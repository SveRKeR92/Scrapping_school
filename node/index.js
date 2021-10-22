const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
      const browser = await puppeteer.launch({
            headless : false, //ouvre le navigateur if false
      });

      const page = await browser.newPage();
      await page.setDefaultNavigationTimeout(0);
      await page.setViewport({width: 1600, height:900});
      await page.goto('https://www.leonard-de-vinci.net/', {waitUntil: 'networkidle2'}); //wait for page to load
      
      // await page.waitForTimeout(1000)
      
      await page.$eval('input[id=login]', e => e.value = 'maxime.attala@edu.devinci.fr');
      await page.$eval('span[id=btn_next]', e => e.click());

      await page.waitForNavigation({waitUntil: 'networkidle2'})
      await page.waitForTimeout(1000)


      await page.$eval('input[id=passwordInput]', e => e.value = 'Password');
      await page.$eval('span[id=submitButton]', e => e.click());

      await page.waitForNavigation({waitUntil: 'networkidle2'})
      await page.waitForTimeout(1000)

      const btnPresence = await page.$x('/html/body/div[1]/div/div/div[5]/div[1]/a[13]')
      // console.log(btnPresence[0])
      await btnPresence[0].click()
      console.log('ok');

      await page.waitForNavigation({waitUntil: 'networkidle2'})
      await page.waitForTimeout(1000)

      const data = await page.$$eval('table tr td', tds => tds.map((td) => {
            return td.innerText;
          }));

      console.log(data)

      const links = []
      for (let index = 0; index < data.length; index++) {
            if ((index+1) % 5 == 0){
                  links.push(data[index])
            }
      }

      console.log(links)

      links.forEach(element => {
            fs.writeFileSync('zoomLinks.txt', element + " \n");
      });

      const linkToAppel = await page.$x('/html/body/div[1]/div/div/div[4]/div/div/div[2]/table/tbody/tr/td[4]/a')
      await linkToAppel[0].click()


      await page.waitForNavigation({waitUntil: 'networkidle2'})
      await page.waitForTimeout(1000)

      await page.screenshot({path: 'img/beforeValidation.png'})
      await page.$eval('span[id=set-presence]', e => e.click())
      await page.screenshot({path: 'img/afterValidation.png'})

      console.log('before zoom')
      const title1 = await page.title()
      console.log(title1)

      const linkToZoom = await page.$x('/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/table/tbody/tr/td[4]/a')

      const [target] = await Promise.all([
            new Promise(resolve => browser.once('targetcreated', resolve)),
            linkToZoom[0].click(),
      ]);
      
      const newPage = await target.page();
      await newPage.bringToFront();


      // await page.waitForNavigation({waitUntil: 'networkidle2'})

      // console.log("before 5 secs")
      await newPage.waitForTimeout(2000)

      console.log('on zoom page')

      await newPage.on('dialog', async dialog => {
            console.log(dialog.message())
            await dialog.accept();
      });

      // await page.waitForTimeout(1000)

      await newPage.keyboard.type(String.fromCharCode(9));
      await newPage.waitForTimeout(1000)
      await newPage.keyboard.type(String.fromCharCode(9));
      await newPage.waitForTimeout(1000)
      await newPage.keyboard.type(String.fromCharCode(13));
      await newPage.keyboard.type(String.fromCharCode(13));

      const title =  await newPage.title()
      console.log(title)
      // await page.type(String.fromCharCode(37));
      // console.log('left')
      // await page.type(String.fromCharCode(13));
      // console.log('enter')



      


      // await page.screenshot({path: 'img/img.png'});
      // await page.$eval('button[type=submit]', e => e.click());
      // await page.waitForNavigation()
      // await page.waitForTimeout(1000)

      // await browser.close();
})();


