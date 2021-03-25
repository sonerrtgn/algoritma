<html>

<body>
    <script>

        //ilkel yontem.
        function aralarinda_asalmi(sayi1,sayi2){
            var bolen = 3;

            if(sayi1 > sayi2){
                var sinir = sayi1/2;
            }else{
                var sinir = sayi2/2;
            }
            if(sayi1 % 2 == 0 && sayi2 %2 == 0){
                return 0;
            }
            while(bolen <= sinir){
                if(sayi1 % bolen == 0 && sayi2 %bolen == 0){
                return 0;
                }
                bolen+=2;
            }
            return 1;
        }
        function phi(n){
            var uygunlar = 1;
            var baslangic = 2;
            while(baslangic < n){
                if(aralarinda_asalmi(baslangic,n) == 1){
                    uygunlar++;
                }
                console.log(baslangic);
                baslangic++;
            }
            return uygunlar
        }
        function nboluphin(hangi_araliga_kadar_kontrol_edilsin){
            var baslangic = 3;
            var max_oran = 0;
            while(baslangic <= hangi_araliga_kadar_kontrol_edilsin){
                if(baslangic/phi(baslangic) > max_oran){
                    max_oran = baslangic/phi(baslangic)
                }
                if(baslangic % 1000 == 0){
                    console.log(baslangic);
                }
                baslangic++;
            }
            return max_oran;
        }


        /*
        Soruda bizden n/aralarında asal nden küçük sayıların sayısı en buyuk değerini istiyor.
        Burada en buyuk değer için n en buyuk olurken aralarında asal olan sayıların sayısı minimumum olmalıdır.
        eğer n 2'ye tam bölünürse 2,4,6,8.... sayıları aralarında asal olmayacağı için 2'nin katları olan tüm sayılar çıkar ve istenen değer dahada büyür.
        eğer n 3'e tam bölünürse  3,6,9,12,15 gibi sayılarla aralırında asal olmayacağı için sayımız artmaya devam eder
        eğer n 5'e tam bölünürse 5 10 15 20 25 gibi sayılarla aralrında asal olmayacağı için büyümeye devam eder aradaki 4'e bakmadık çünkü 2 ye bölünüyorsa ararlarında zaten asal olmaz.
        yukarıda görüldüğü gibi eğer n kendinden küçük asallara tam olarak bölünürse neredeyse aralarındaki asalların sayısı 1'olur.
        o zaman n=2.3.5.7.11.13.17.19... ve n< 10^6 olacak n sayısı en büyük bölümü verir
        */
       // gelişmiş yöntem
        function asalmi(x){
            var bolen = 3;
            var durak = Math.sqrt(x);
            if(x%2 == 0 && x==2){
                return 1;
            }
            if(x%2 == 0){
                return 0;
            }
            
            while(bolen <= durak){
                if(x%bolen == 0){
                    return 0;
                }
                bolen+=2;
            }
            return 1;
        }
       function asal_a(x){
            //x.inci asalı bulan fonksyion
            if(x==1){
                return 2;
            }
            var baslangic = 3;
            var count = 2;
            while(count < x){
                if(asalmi(baslangic)==1){
                    count++;
                }
                baslangic+=2;
            }
            return baslangic-2;
        }
        function aralarinda_asali_minumum_olan_sayi(){
            var sayi = 1;
            var count= 1;
            while(sayi <1000000){
                sayi *= asal_a(count);
                count++;
            }
            if(sayi>1000000){
                sayi = sayi/asal_a(count-1);
            }
            return sayi;
        }
        function phiorani(hangi_sayiya_bakilsin){
            return hangi_sayiya_bakilsin/phi(hangi_sayiya_bakilsin);
        }
        console.log(aralarinda_asali_minumum_olan_sayi());

    </script>
</body>
</html>
