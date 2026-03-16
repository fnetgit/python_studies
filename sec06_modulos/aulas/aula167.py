# Locale para internacionalização

import locale
import calendar

locale.setlocale(locale.LC_ALL, "")  # padrão do sistema
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
print(calendar.month(2026, 3))

# locale -a
