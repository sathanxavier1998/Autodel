#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = "6620972"
API_HASH     = "3f6835286b03e000ab6d71b37cc35b92"
BOT_TOKEN    = "5020137731:AAFMBHWEvsZnfoOA5vY33rJiSJPPOA-Ccn8"
SESSION      = "BQBlBywAkgqoirSOtonpTj2beSLdhb6m_Ez0KudNdQ5YhkxPvgiIb8euUCLISLrk_U3B0JiRZinYJvYv7V1Fs_fMFQxEHcNsY4wxsCEGSMZ3XhIWJyOgc_VlpzSiwcwLGcIQqM4qLpNWfFgMj2FrJgf2tzFkK9-ODV6DD4QzQMI6q8SoIQJn8JZMF3k9xJZFMJbLEN9BCbhGBirdWmJyUp5WO07jw8_fRjrO1QvUIbxsWCvhlaHrPu24I19J8Y9sHt2WNm_vF9ID-qBcF0OKb0MlKiy_5BByaN6tIjtB7ZIPW_V8m7Eo8_2-Fp7LIF7O-cC1sLuni5wW6pjdGUNymVfR0GBQAAAABoA08GAA"
TIME         = "190"
CHATS        = "-1001570401050"
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"
PORT         = "8080"
