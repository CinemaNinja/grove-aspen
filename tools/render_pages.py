#!/usr/bin/env python3
"""Write the static Grove Aspen pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("About", "/about/", "about"),
    ("Membership", "/membership/", "membership"),
    ("Programming", "/programming/", "programming"),
    ("Private events", "/private-events/", "events"),
    ("Gallery", "/gallery/", "gallery"),
]

def head(title, description, path, current=None):
    nav = []
    for label, href, key in NAV:
        current_attr = ' aria-current="page"' if key == current else ""
        nav.append(f'<a href="{href}"{current_attr}>{label}</a>')
    nav_html = "\n        ".join(nav)
    canonical = f"https://www.groveaspen.club{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#1B3129">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Grove">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://www.groveaspen.club/assets/og/social.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.ico">
  <link rel="icon" type="image/png" href="/assets/logo/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/logo/apple-touch.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <a class="brand" href="/" aria-label="Grove home">
      <img src="/assets/logo/wordmark.png" alt="Grove" width="150" height="50">
    </a>
    <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="site-nav" data-nav>
        {nav_html}
        <a class="nav-cta" href="/contact/">Contact</a>
    </nav>
  </header>
  <main id="main">
"""

FOOT = """
  </main>
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <img src="/assets/logo/wordmark.png" alt="" width="140" height="47">
        <p>A gathering place<br>315 E. Hyman Avenue<br>Aspen, Colorado</p>
        <p>Member hours, 7am–6pm daily.<br>Evenings belong to programming.</p>
      </div>
      <div>
        <p class="kicker">Visit</p>
        <ul>
          <li><a href="/about/">About</a></li>
          <li><a href="/membership/">Membership</a></li>
          <li><a href="/programming/">Programming</a></li>
          <li><a href="/private-events/">Private events</a></li>
          <li><a href="/gallery/">Gallery</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <p class="kicker">Sign up for news and events</p>
        <form data-form data-store="grove-newsletter" data-subject="Grove news">
          <label>
            <span>Email address</span>
            <input type="email" name="email" placeholder="Email address" required autocomplete="email">
          </label>
          <button class="btn" type="submit">Sign up</button>
          <p class="note" data-success hidden>Thank you.</p>
        </form>
      </div>
    </div>
    <div class="wrap legal">
      <span>Grove · Aspen</span>
      <a href="/privacy/">Privacy</a>
    </div>
  </footer>
  <div class="lightbox" data-lightbox>
    <button type="button" data-lightbox-close>Close</button>
    <img alt="">
  </div>
  <script src="/js/site.js"></script>
</body>
</html>
"""

def page(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html.strip() + "\n", encoding="utf-8")
    print(rel)

GALLERY = [
    ("/assets/gallery/r6a00586.jpg", "Lounge seating at The Grove, with boucle chairs and a shared rug"),
    ("/assets/gallery/r6a00584.jpg", "Inside The Grove"),
    ("/assets/gallery/r6a00643.jpg", "A room at The Grove"),
    ("/assets/gallery/r6a00623.jpg", "Gathering space at The Grove"),
    ("/assets/gallery/r6a00594.jpg", "Seating at The Grove"),
    ("/assets/gallery/r6a00590.jpg", "The Grove interior"),
    ("/assets/gallery/r6a00709.jpg", "Daylight inside The Grove"),
    ("/assets/gallery/r6a00701.jpg", "Tables and lounge at The Grove"),
    ("/assets/gallery/r6a00698.jpg", "A corner of The Grove"),
    ("/assets/gallery/r6a00712.jpg", "The Grove, ready for company"),
]

EVENTS = [
    ("/assets/events/3e1a9330.jpg", "Private lounge with a sofa, timber tables, and a ski photograph"),
    ("/assets/events/3e1a9325.jpg", "Private event space at The Grove"),
    ("/assets/events/3e1a9331.jpg", "Private event seating at The Grove"),
    ("/assets/events/3e1a9336.jpg", "A room set for a private gathering"),
    ("/assets/events/3e1a9338.jpg", "Lounge arranged for a private event"),
    ("/assets/events/3e1a9342.jpg", "Private event interior at The Grove"),
    ("/assets/events/3e1a9348.jpg", "Seating for a private gathering"),
    ("/assets/events/3e1a9352.jpg", "Details of the private event rooms"),
    ("/assets/events/3e1a9354.jpg", "A quiet corner for a private meeting"),
    ("/assets/events/3e1a9357.jpg", "Private event lounge"),
    ("/assets/events/3e1a9359.jpg", "The Grove set for guests"),
    ("/assets/events/3e1a9361.jpg", "Private gathering space"),
    ("/assets/events/3e1a9365.jpg", "Event seating at The Grove"),
    ("/assets/events/3e1a9404.jpg", "A wider view of the private rooms"),
    ("/assets/events/3e1a9597.jpg", "Private event space in the heart of Aspen"),
]

def mosaic(items):
    links = []
    for src, alt in items:
        links.append(f'<a data-zoom href="{src}"><img src="{src}" alt="{alt}"></a>')
    return "\n          ".join(links)

page("index.html", head(
    "Grove — A Gathering Place",
    "The Grove is a gathering place in Aspen for local membership, the lounge, and community events. 315 E. Hyman Avenue.",
    "/",
) + """
    <section class="hero">
      <div>
        <img class="hero-mark" src="/assets/logo/combination.png" alt="Grove">
        <h1>Take root with us.</h1>
        <p class="kicker" style="margin-top:1.4rem">Now open</p>
        <p class="hero-lead">Join us at the Grove. Local membership, lounge, events.</p>
        <div class="hero-actions">
          <a class="btn" href="/contact/?topic=tour">Schedule a tour</a>
          <a class="btn ghost" href="/membership/">Membership</a>
        </div>
      </div>
    </section>
    <section class="band">
      <div class="facts wrap">
        <div>Local membership</div>
        <div>Lounge</div>
        <div>Events</div>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap split">
        <div class="frame">
          <img src="/assets/gallery/r6a00586.jpg" alt="Lounge seating at The Grove">
        </div>
        <div class="copy">
          <p class="kicker">Grove Aspen</p>
          <h2>An invitation to gather</h2>
          <p>The Grove is open to the Aspen community: somewhere to work, learn, meet, and belong. An unhurried home base in the center of Aspen, open through the working day and alive with community in the evenings.</p>
          <p>It is built for the people who make this town what it is: makers, founders, practitioners, and neighbors who do their best work in good company.</p>
          <a class="btn" href="/about/">About the Grove</a>
        </div>
      </div>
    </section>
    <section class="section canopy">
      <div class="wrap">
        <div class="pillars">
          <article class="card">
            <p class="index">01</p>
            <h3>Workspace</h3>
            <p>A daytime workspace for people who work for themselves but would rather not work by themselves — from morning light to evening.</p>
          </article>
          <article class="card">
            <p class="index">02</p>
            <h3>Lounge</h3>
            <p>A wide array of seating, tables, and lounges. Ideal for taking meetings, catching up, and sharing time. This is the living room for us all.</p>
          </article>
          <article class="card">
            <p class="index">03</p>
            <h3>Programming</h3>
            <p>Dance and movement. Mindfulness and art. Music and games. This is the Grove’s weekly lineup. A space where activities are what bring us together.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section deep" id="look">
      <div class="wrap film">
        <div class="section-head">
          <p class="kicker">Take a look around</p>
          <h2>Aspen, from above the grove.</h2>
          <p class="lede">A short film of town, then the rooms themselves.</p>
        </div>
        <video controls preload="metadata" poster="/assets/video/poster.jpg">
          <source src="/assets/video/look-around.mp4" type="video/mp4">
        </video>
        <p class="caption">Two minutes. Press play.</p>
        <div class="reel">
          """ + mosaic(GALLERY[:6]) + """
        </div>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Membership</p>
          <h2>A locals’ living room.</h2>
          <p class="lede">A membership for Aspen’s locals and part-time locals. A space for work and meetings, a lounge for connecting and catching up, a place to gather and create together.</p>
        </div>
        <div class="tiers">
          <article class="tier">
            <header>
              <p class="kicker">Coworking</p>
              <h3>Coworking membership</h3>
              <p>For locals who need a place to work, meet, and land during the week.</p>
              <p class="price">$3,000 <span>per year</span></p>
            </header>
            <a class="btn" href="/apply/?tier=coworking">Apply · Coworking</a>
          </article>
          <article class="tier featured">
            <header>
              <p class="kicker">Patron</p>
              <h3>Patron membership</h3>
              <p>Everything in Coworking, plus evenings, private use, and a hand in keeping the Grove open to all.</p>
              <p class="price">$6,000 <span>per year</span></p>
            </header>
            <a class="btn" href="/apply/?tier=patron">Apply · Patron</a>
          </article>
        </div>
      </div>
    </section>
""" + FOOT)

page("about/index.html", head(
    "About — Grove",
    "The Grove is an unhurried home base in the center of Aspen for work, the lounge, and community programming.",
    "/about/",
    "about",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Grove Aspen</p>
        <h1>An invitation to gather</h1>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap prose">
        <p>The Grove is open to the Aspen community: somewhere to work, learn, meet, and belong. An unhurried home base in the center of Aspen, open through the working day and alive with community in the evenings.</p>
        <p>It is built for the people who make this town what it is: makers, founders, practitioners, and neighbors who do their best work in good company.</p>
        <p>The Grove is a deliberate answer to what Aspen has been missing. Somewhere to linger without a reservation, a reason to come downtown without a transaction, a place to support and grow ideas.</p>
        <p><strong style="color:var(--cream);font-weight:500">This is not another luxury storefront. This is a place for locals to gather.</strong></p>
      </div>
    </section>
    <section class="section canopy">
      <div class="wrap split">
        <div class="frame"><img src="/assets/gallery/r6a00709.jpg" alt="Inside The Grove"></div>
        <div class="stack">
          <article class="card">
            <h3>Workspace</h3>
            <p>A daytime workspace for people who work for themselves but would rather not work by themselves — from morning light to evening.</p>
          </article>
          <article class="card">
            <h3>Lounge</h3>
            <p>A wide array of seating, tables, and lounges. Ideal for taking meetings, catching up, and sharing time. This is the living room for us all.</p>
          </article>
          <article class="card">
            <h3>Programming</h3>
            <p>Dance and movement. Mindfulness and art. Music and games. This is the Grove’s weekly lineup. A space where activities are what bring us together.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section deep">
      <div class="wrap split reverse">
        <div class="copy">
          <p class="quote">It shines above. It connects below. So do we.</p>
          <a class="btn" href="/membership/">See membership</a>
        </div>
        <div class="frame"><img src="/assets/events/3e1a9330.jpg" alt="Lounge at The Grove with a sofa and timber tables"></div>
      </div>
    </section>
""" + FOOT)

page("membership/index.html", head(
    "Membership — Grove",
    "Coworking membership is $3,000 a year. Patron membership is $6,000 a year. Weekday access, the lounge, wi-fi, coffee, and community programming at The Grove in Aspen.",
    "/membership/",
    "membership",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Membership</p>
        <h1>A locals’ living room</h1>
        <p class="lede">A membership for Aspen’s locals and part-time locals. A space for work and meetings, a lounge for connecting and catching up, a place to gather and create together.</p>
        <div class="hero-actions" style="justify-content:flex-start">
          <a class="btn" href="https://members.groveaspen.club/account/memberships/change">Apply for membership</a>
          <a class="btn ghost" href="/apply/">Read the agreement</a>
        </div>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap split">
        <div class="copy">
          <p class="kicker">Why Grove</p>
          <h2>Aspen has lost its third spaces. The Grove brings one back.</h2>
          <p>3,000 square feet built for gathering — a space for work and meetings, a lounge for connecting and catching up, a place to gather and create together.</p>
        </div>
        <div>
          <p class="kicker" style="margin-bottom:0.8rem">What every membership includes</p>
          <ol class="amenity-list">
            <li><span class="index">01</span><div><strong>Weekday access</strong><br>Work, meetings, and the lounge, 7am–6pm</div></li>
            <li><span class="index">02</span><div><strong>Reserved member spots</strong><br>A held seat at every community program</div></li>
            <li><span class="index">03</span><div><strong>Member-only events</strong><br>Evenings and gatherings just for members</div></li>
            <li><span class="index">04</span><div><strong>Flexible seating</strong><br>Tables, soft seating, and power everywhere</div></li>
            <li><span class="index">05</span><div><strong>Fast wi-fi</strong><br>Built for real work and video calls</div></li>
            <li><span class="index">06</span><div><strong>Coffee, tea &amp; matcha</strong><br>Complimentary, all day</div></li>
            <li><span class="index">07</span><div><strong>Bookable meeting rooms</strong><br>Reserve space for clients and teams</div></li>
          </ol>
        </div>
      </div>
    </section>
    <section class="section canopy">
      <div class="wrap tiers">
        <article class="tier">
          <header>
            <p class="kicker">Coworking</p>
            <h3>Coworking membership</h3>
            <p>For locals who need a place to work, meet, and land during the week.</p>
            <p class="price">$3,000 <span>per year</span></p>
          </header>
          <ul class="check-list">
            <li><span class="index">—</span><span>Weekday access for work, meetings, and lounge</span></li>
            <li><span class="index">—</span><span>A reserved spot for all community programming</span></li>
            <li><span class="index">—</span><span>Exclusive member-only events</span></li>
            <li><span class="index">—</span><span>Fast, reliable wi-fi</span></li>
            <li><span class="index">—</span><span>Complimentary coffee, tea, and matcha all day</span></li>
            <li><span class="index">—</span><span>Bookable meeting spaces</span></li>
          </ul>
          <a class="btn" href="/apply/?tier=coworking">Apply · Coworking</a>
        </article>
        <article class="tier featured">
          <header>
            <p class="kicker">Patron</p>
            <h3>Patron membership</h3>
            <p>Everything in Coworking, plus evenings, private use, and a hand in keeping the Grove open to all.</p>
            <p class="price">$6,000 <span>per year</span></p>
          </header>
          <ul class="check-list">
            <li><span class="index">—</span><span>Everything in Coworking</span></li>
            <li><span class="index">—</span><span>Access to intimate Grove Evening experiences</span></li>
            <li><span class="index">—</span><span>Book the space for private use (restrictions apply)</span></li>
            <li><span class="index">—</span><span>Funds the Scholarship Member program</span></li>
            <li><span class="index">—</span><span>Recognition as a Patron Member of Grove Aspen</span></li>
          </ul>
          <a class="btn" href="/apply/?tier=patron">Apply · Patron</a>
        </article>
      </div>
    </section>
""" + FOOT)

page("programming/index.html", head(
    "Programming — Grove",
    "A 2,000-square-foot room at The Grove for movement, workshops, meet-ups, wellness, talks, and gatherings. See the Aspen Arts Club calendar.",
    "/programming/",
    "programming",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Programming</p>
        <h1>Bring what you know. Teach it here.</h1>
        <p class="lede">At the heart of The Grove is a 2,000-square-foot room where Aspen Arts Club brings its programming to life and invites collaboration with local practitioners. Teach a skill, lead a class, host a meet-up or gathering, or offer instruction of any kind. If you have something to share, the room is yours.</p>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap offers">
        <article class="offer">
          <p class="index">Move</p>
          <h3>Movement &amp; practice</h3>
          <p>Yoga, breathwork, somatics — the quieter disciplines that need open floor.</p>
        </article>
        <article class="offer">
          <p class="index">Make</p>
          <h3>Workshops &amp; classes</h3>
          <p>Hands-on instruction in a craft, a trade, a language, or a tool worth learning.</p>
        </article>
        <article class="offer">
          <p class="index">Meet</p>
          <h3>Meet-ups &amp; clubs</h3>
          <p>Recurring gatherings for the groups and interests that hold the town together.</p>
        </article>
        <article class="offer">
          <p class="index">Tend</p>
          <h3>Wellness &amp; care</h3>
          <p>Practitioners offering instruction and sessions that help the community thrive.</p>
        </article>
        <article class="offer">
          <p class="index">Listen</p>
          <h3>Talks &amp; readings</h3>
          <p>Conversations, lectures, and readings that bring people into one room.</p>
        </article>
        <article class="offer">
          <p class="index">Gather</p>
          <h3>Gatherings of any kind</h3>
          <p>Whatever a community needs a generous, welcoming room to do together.</p>
        </article>
      </div>
    </section>
    <section class="section canopy">
      <div class="wrap split">
        <div class="frame"><img src="/assets/programming/img2778.jpg" alt="A gathering watching a talk at The Grove"></div>
        <div class="copy">
          <p class="kicker">2,000</p>
          <h2>Square feet for the community.</h2>
          <p>See what events are coming up. The Grove calendar lives with Aspen Arts Club.</p>
          <p>Have something to teach or share? The room is open to the whole grove.</p>
          <div class="hero-actions" style="justify-content:flex-start">
            <a class="btn" href="https://www.aspenartsclub.org/calendar">Grove calendar</a>
            <a class="btn ghost" href="/contact/?topic=session">Propose a session</a>
          </div>
        </div>
      </div>
    </section>
    <section class="section deep">
      <div class="wrap reel">
        """ + mosaic([
            ("/assets/programming/r6a00643.jpg", "Programming room at The Grove"),
            ("/assets/programming/r6a00584.jpg", "The Grove arranged for a session"),
            ("/assets/programming/img7435.jpg", "Community programming at The Grove"),
            ("/assets/programming/img2778.jpg", "People gathered for a talk at The Grove"),
        ]) + """
      </div>
    </section>
""" + FOOT)

page("private-events/index.html", head(
    "Private events — Grove",
    "Limited private events at The Grove, 315 E. Hyman Avenue in Aspen. 1,000 to 3,000 square feet of lounge and meeting space.",
    "/private-events/",
    "events",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Grove Aspen</p>
        <h1>Looking for private event space in the heart of Aspen?</h1>
        <p class="lede">Our space is available for a limited number of private events each month. From 1,000–3,000 square feet of fully equipped lounge and meeting space is available for a variety of events, meetings, and experiences.</p>
        <p class="lede">If you’re interested in hosting your event at The Grove, send us a note with the details.</p>
        <div class="hero-actions" style="justify-content:flex-start">
          <a class="btn" href="/contact/?topic=private">Contact us</a>
        </div>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap mosaic">
        """ + mosaic(EVENTS) + """
      </div>
    </section>
""" + FOOT)

page("gallery/index.html", head(
    "Gallery — Grove",
    "Rooms at The Grove in Aspen: workspace, lounge, and gathering space.",
    "/gallery/",
    "gallery",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Gallery</p>
        <h1>Room to do your best work, in good company.</h1>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap mosaic">
        """ + mosaic(GALLERY) + """
      </div>
    </section>
    <section class="section canopy">
      <div class="wrap visit">
        <div>
          <h2>Interested in joining?</h2>
          <p class="lede">Reach out to learn about membership opportunities.</p>
        </div>
        <a class="btn" href="/contact/?topic=membership">Get in touch</a>
      </div>
    </section>
""" + FOOT)

page("contact/index.html", head(
    "Contact — Grove",
    "Contact The Grove at 315 E. Hyman Avenue, Aspen, about the workspace, a tour, an event idea, or a private event.",
    "/contact/",
    "contact",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Contact</p>
        <h1>Write to the Grove.</h1>
        <p class="lede">Contact us to learn more about the workspace, pitch an idea for an event, reach out about a private event inquiry, or learn how to get involved with The Grove.</p>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap visit">
        <form data-form data-store="grove-contact" data-subject="Note for the Grove">
          <div class="form-row">
            <label><span>Name</span><input name="name" required autocomplete="name"></label>
            <label><span>Email</span><input type="email" name="email" required autocomplete="email"></label>
          </div>
          <label><span>Phone</span><input type="tel" name="phone" autocomplete="tel"></label>
          <label>
            <span>This note is about</span>
            <select name="topic" data-topic required>
              <option value="tour">Schedule a tour</option>
              <option value="membership">Membership</option>
              <option value="session">Propose a session</option>
              <option value="private">Private event</option>
              <option value="general">Something else</option>
            </select>
          </label>
          <label><span>Note</span><textarea name="message" required></textarea></label>
          <button class="btn" type="submit">Send the note</button>
          <p class="note" data-success hidden>Thank you. Your note is kept on this device. Bring it with you to 315 E. Hyman Avenue, or continue through member enrollment.</p>
        </form>
        <aside class="copy">
          <p class="kicker">A gathering place</p>
          <p class="quote" style="font-size:2rem">315 E. Hyman Avenue, Aspen, Colorado</p>
          <p>Member hours are 7am to 6pm daily. Evening programming is scheduled separately.</p>
          <p><a href="https://maps.google.com/?q=315+E+Hyman+Avenue+Aspen+Colorado">Open in maps</a></p>
          <p><a href="https://members.groveaspen.club/account/memberships/change">Member enrollment</a></p>
        </aside>
      </div>
    </section>
""" + FOOT)

AGREEMENT = """
<div class="agreement">
  <p class="kicker">The Grove — a gathering place</p>
  <h2 style="font-size:1.8rem">Membership agreement</h2>
  <p>This Membership Agreement (the “Agreement”) is entered into between The Grove (the “Club”), located at 315 E. Hyman Avenue, Aspen, Colorado, and the individual identified in the signature block below (the “Member”), effective as of the date of the Member’s enrollment.</p>
  <h3>1. Membership &amp; tiers</h3>
  <p>The Grove offers Coworking and Patron annual memberships, described above. Membership fees are billed annually at the rates then in effect and are due in full upon enrollment and each renewal. Membership is personal to the Member and may not be shared, assigned, or transferred.</p>
  <h3>2. Access &amp; operating hours</h3>
  <p>The workspace is available to members from 7:00 AM to 6:00 PM daily (“operating hours”). The Club may adjust operating hours, close the space for private events or programming, or modify access from time to time. Access is granted through the Club’s membership application and credential system. The Member is responsible for safeguarding their credentials and may not share them or admit others to the space using their access.</p>
  <h3>3. Use of the space</h3>
  <p>The space is reserved for work and meetings. The Member agrees to use the workspace for its intended purpose and to respect operating hours and evening programming. Remaining in the space past operating hours is not permitted, except in connection with scheduled programming the Member is attending. Bringing guests into the space after operating hours is a violation of this Agreement.</p>
  <h3>4. Included amenities</h3>
  <p>All members are provided with wifi and complimentary coffee, tea, sparkling water, and hot water while in the space, along with use of the shared workspace, lounge, and common areas during operating hours.</p>
  <h3>5. Guests</h3>
  <p>Members may bring guests for meetings only. Guests are expected to leave at the conclusion of the meeting and may not use the space as a workspace. Access to wifi is reserved for members only. Guests must comply with this Agreement and the Community Principles, and the Member remains responsible for their guest’s conduct. Guests are not permitted after operating hours.</p>
  <h3>6. Club private events</h3>
  <p>The Club will use the entire space for private events up to seven (7) times annually; during these events members will not have access. Such closures will not exceed four (4) days over a peak weekend. The Club will give advance notice where reasonably possible. Member requests for private use are considered case-by-case, at the Club’s discretion, and may involve additional fees and a separate agreement.</p>
  <h3>7. Community principles</h3>
  <p>An aspen grove looks like many trees, but it is one organism — every trunk rising from a single, shared root system. The Grove works the same way. These principles are how we keep our shared space healthy, welcoming, and worth returning to. Membership means agreeing to live by them.</p>
  <p><strong>Respect the space.</strong> Leave it as you found it, or better. Clean up after yourself, reset what you use, and clear your area when you go.</p>
  <p><strong>Respect each other.</strong> This is a place for focused work in good company. Be mindful of noise and take calls with headphones.</p>
  <p><strong>Respect access.</strong> Your membership and credentials are yours alone. Guests are welcome for meetings only, and you’re responsible for any guest you host.</p>
  <p><strong>Honor the hours.</strong> 7 AM to 6 PM, with no after-hours access except scheduled programming you’re attending.</p>
  <p><strong>Care for what’s shared.</strong> Use the wifi and amenities generously and reset stations for the next member. Treat furnishings and the building with care.</p>
  <p><strong>Add to the Grove.</strong> Welcome newcomers, look out for one another, and contribute to the kind of community you’d want to be part of.</p>
  <p>The Member agrees to abide by these Community Principles, which form part of this Agreement.</p>
  <h3>8. Assumption of risk &amp; release of liability</h3>
  <p>The Member uses the space, amenities, and programming at their own risk. To the fullest extent permitted by law, the Member releases and holds harmless the Club, its owners, employees, and agents from any liability for injury, illness, loss, or damage arising from the Member’s use of the premises, amenities, or programming, except to the extent caused by the Club’s gross negligence or willful misconduct.</p>
  <h3>9. Responsibility for damage</h3>
  <p>The Member is responsible for any damage to the premises, furnishings, equipment, or property of the Club or other members caused by the Member or the Member’s guests, and agrees to reimburse the Club for the cost of repair or replacement.</p>
  <h3>10. Termination, violations &amp; refunds</h3>
  <p>The Club may terminate this membership immediately if the Member violates this Agreement or the Community Principles. Upon termination for a violation, the Member’s access ends immediately and no refund of any membership fee will be provided. All decisions by the Club regarding violations and termination are final and binding, and are not subject to appeal. The Club may also modify or discontinue amenities, programming, or membership terms; material changes will be communicated to members.</p>
  <h3>11. Media release</h3>
  <p>The Member grants the Club permission to use photographs and recordings taken in the space that may include the Member for the Club’s ordinary marketing and community purposes. A Member may opt out by notifying the Club in writing.</p>
  <h3>12. General</h3>
  <p>This Agreement is governed by the laws of the State of Colorado. If any provision is found unenforceable, the remaining provisions remain in effect. This Agreement, including the Community Principles in Section 7, constitutes the entire agreement between the Member and the Club regarding membership.</p>
</div>
"""

page("apply/index.html", head(
    "Membership application — Grove",
    "Join The Grove. Read the membership agreement, choose Coworking or Patron, and continue to enrollment.",
    "/apply/",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">The Grove — membership</p>
        <h1>Join the Grove</h1>
        <p class="lede">A gathering place and shared workspace in Aspen — built on the idea that a grove looks like many trees, but shares one root system. Membership means becoming part of it.</p>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap" style="display:grid;gap:1.4rem">
        """ + AGREEMENT + """
        <form data-form data-store="grove-applications" data-subject="Grove membership agreement" data-next="/apply/received/">
          <fieldset style="border:0;padding:0;margin:0;display:grid;gap:0.75rem">
            <legend class="kicker">Membership tier</legend>
            <p class="caption">Choose the membership that fits how you’ll use the space.</p>
            <label class="check"><input type="radio" name="tier" value="Coworking" data-tier required> <span><strong style="color:var(--cream)">Coworking membership.</strong> Access to the workspace during operating hours (7 AM – 6 PM daily) and all shared amenities — wifi, coffee, tea, lounge, and common areas.</span></label>
            <label class="check"><input type="radio" name="tier" value="Patron"> <span><strong style="color:var(--cream)">Patron membership.</strong> All Coworking benefits, plus access to all special evening programming and events, and your membership helps support the Club’s community scholarship program.</span></label>
          </fieldset>
          <p class="kicker">Your details</p>
          <div class="form-row">
            <label><span>Full name</span><input name="name" required autocomplete="name"></label>
            <label><span>Email address</span><input type="email" name="email" required autocomplete="email"></label>
          </div>
          <label><span>Phone number</span><input type="tel" name="phone" required autocomplete="tel"></label>
          <p class="kicker">Membership agreement</p>
          <p class="caption">Please read in full before signing.</p>
          <label class="check"><input type="checkbox" name="agreed" value="yes" required> <span>I have read and agree to this Membership Agreement, including the Community Principles.</span></label>
          <div class="form-row">
            <label><span>Signature (type full name)</span><input name="signature" required></label>
            <label><span>Date</span><input type="date" name="date" data-today required></label>
          </div>
          <button class="btn" type="submit">Join the Grove</button>
          <p class="caption">You’ll receive a confirmation and enrollment details by email once the club processes the agreement. Finish enrollment in the member portal if you are ready now.</p>
          <p><a href="https://members.groveaspen.club/account/memberships/change">Continue in the member portal</a></p>
        </form>
      </div>
    </section>
""" + FOOT)

page("apply/received/index.html", head(
    "Welcome to the Grove",
    "Your Grove membership agreement is saved. Continue to the member portal to finish enrollment.",
    "/apply/received/",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Welcome to the Grove</p>
        <h1>Your agreement is signed.</h1>
        <p class="lede">Signed by <span data-member-name>you</span>.</p>
        <p class="lede">The Grove is a gathering place and shared workspace in Aspen — built on the idea that a grove looks like many trees, but shares one root system. Membership means becoming part of it.</p>
        <p class="lede">Look out for an email with your credentials and enrollment details once the club receives this agreement. Continue in the member portal to finish.</p>
        <div class="hero-actions" style="justify-content:flex-start">
          <a class="btn" href="https://members.groveaspen.club/account/memberships/change">Member portal</a>
          <button class="btn ghost" type="button" data-copy-last>Copy your agreement</button>
        </div>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap">
        <pre class="agreement" data-last-note style="white-space:pre-wrap"></pre>
      </div>
    </section>
""" + FOOT)

page("privacy/index.html", head(
    "Privacy — Grove",
    "How The Grove uses notes, membership details, and newsletter addresses you leave on this site.",
    "/privacy/",
) + """
    <section class="page-hero">
      <div class="wrap">
        <p class="kicker">Privacy</p>
        <h1>What you send stays with the Grove.</h1>
      </div>
    </section>
    <section class="section grove">
      <div class="wrap prose">
        <p>Notes, tour requests, session proposals, private-event inquiries, newsletter addresses, and membership agreements are used to respond to you and to run The Grove at 315 E. Hyman Avenue, Aspen, Colorado.</p>
        <p>Until a club inbox is connected, this website keeps those notes in your own browser. They are not sold. Photographs and recordings in the space may be used for the club’s ordinary marketing, and a member may opt out in writing, as the membership agreement describes.</p>
        <p>To ask for a note to be removed, write through the contact page or tell the club in person.</p>
        <p><a href="/contact/">Contact</a></p>
      </div>
    </section>
""" + FOOT)

page("404.html", head(
    "Page not found — Grove",
    "That page is not on The Grove site.",
    "/404.html",
) + """
    <section class="hero">
      <div>
        <p class="kicker">404</p>
        <h1>This path doesn’t root here.</h1>
        <p class="hero-lead">The page is missing. The Grove is still at 315 E. Hyman.</p>
        <div class="hero-actions">
          <a class="btn" href="/">Back home</a>
          <a class="btn ghost" href="/contact/">Contact</a>
        </div>
      </div>
    </section>
""" + FOOT)

# Fix radio preselect: data-tier on a radio doesn't work with the JS which sets .value
# The JS sets tierField.value if the element is a select. Radios need a different handler.
# Leave JS as-is and add a tiny inline? Better update site.js after.

print("done")
