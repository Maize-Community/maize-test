import { useMemo } from 'react';
import type { Wallet } from '@maize/api';
import { WalletType } from '@maize/api';
import BigNumber from 'bignumber.js';
import { mojoToCATLocaleString, mojoToMaizeLocaleString, useLocale } from '@maize/core';

export default function useWalletHumanValue(wallet: Wallet, value?: string | number | BigNumber, unit?: string): string {
  const [locale] = useLocale();
  
  return useMemo(() => {
    if (wallet && value !== undefined) {
      const localisedValue = wallet.type === WalletType.CAT
        ? mojoToCATLocaleString(value, locale)
        : mojoToMaizeLocaleString(value, locale);

      return `${localisedValue} ${unit}`;
    }

    return '';
  }, [wallet, value, unit, locale]);
}
