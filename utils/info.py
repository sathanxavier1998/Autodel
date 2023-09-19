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
SESSION      = "BQBnvSqqRW9Sl2Xookw_syX14ThkgM0O1G61ecrlcl7YA372bQHeUqWY3uF6Kuz6K8FD1NCTsWx_b_KaEVb1YHXMXGcYvWZUap_YpwwPAsn4LqiBsmty8HBQVaHOlEl4BYS_WgyQKmC7xKMYh9FILu5afqSleRvPWAeTFWO-TSnuOgZSgdWJvHcs1uPGtSRTmMAZX7RYSeNLXy9yOkmudlSIf453WkNGwHKyQsk0yxlyp8tX-gfTXEexATB_dnkpZfyQ4GktjXkEw1ez-YUFCWTMqqF2YZKseohyT4Z897Y119Muf1V_dYI8sMeasH5VgPc6u-4Zni_F8oIbfKsMkQD3aANPBgA"
TIME         = "190"
CHATS        = "-1001570401050"
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority"
PORT         = "8080"
