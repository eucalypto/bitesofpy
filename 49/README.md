## [Bite 49. Scrape Packt's html with BeautifulSoup](https://codechalleng.es/bites/49/)

The variable book stores this part of the html:

```html
<div class="dotd-main-book cf">
 <div class="section-inner">
  <div class="dotd-main-book-image float-left">
   <a href="/application-development/mastering-typescript-second-edition">
    <noscript>
     <img alt="" class="bookimage imagecache imagecache-dotd_main_image" itemprop="url" src="//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png" title=""/>
    </noscript>
    <img alt="" class="bookimage imagecache imagecache-dotd_main_image" data-original="//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png" itemprop="url" src="/sites/default/files/blank.gif" title=""/>
   </a>
  </div>
  <div class="dotd-main-book-summary float-left">
   <div class="eighteen-days-countdown-bar">
    Time is running out to claim this free ebook
    <span class="packt-js-countdown" data-countdown-to="1519516800">
    </span>
   </div>
   <div class="dotd-title">
    <h2>
     Mastering TypeScript - Second Edition
    </h2>
   </div>
   <br/>
   <div>
    Build enterprise-ready, industrial-strength web applications using TypeScript and leading JavaScript frameworks
   </div>
   <div>
    <ul>
     <li>
      Start with the basics, then enhance your knowledge with in-depth discussions on language features, third-party libraries, design patterns and more
     </li>
     <li>
      Practical examples that show how to use TypeScript with popular frameworks, including Backbone, Angular 2, React, Aurelia, Node and others
     </li>
     <li>
      Focus on test-driven development to build high quality applications that are modular, scalable and adaptable
     </li>
    </ul>
   </div>
   <div class="dotd-main-book-form cf">
    <div class="dots-main-book-price float-left">
    </div>
    <div class="float-left free-ebook">
     <form action="/freelearning-claim/25316/21478" id="free-learning-form" method="POST">
      <div class="twelve-days-claim" id="packt-freelearning-submit-claim">
       <div class="book-claim-token-inner">
        <div class="book-claim-token-logo">
        </div>
        <div class="book-claim-token-separator">
        </div>
        <input class="form-submit" id="free-learning-claim" type="submit" value="Claim Your Free eBook"/>
       </div>
      </div>
      <div id="popup-recaptcha">
      </div>
     </form>
    </div>
   </div>
  </div>
 </div>
</div>
```
