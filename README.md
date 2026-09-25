# Grove Aspen

A rebuild of [groveaspen.club](https://www.groveaspen.club/): membership, programming, private events, gallery, the membership agreement, and the Aspen film.

Colors and copy come from the current club site. The layout is a faster static site.

Preview locally:

```bash
python3 -m http.server 8765
```

Then open `http://127.0.0.1:8765/`.

Notes and the membership agreement are saved in the visitor’s browser until a club inbox is set. Put that address in `CLUB_INBOX` at the top of `js/site.js` and the forms will open a mail draft as well.

Enrollment still continues at [members.groveaspen.club](https://members.groveaspen.club/account/memberships/change). The event calendar stays with [Aspen Arts Club](https://www.aspenartsclub.org/calendar).
