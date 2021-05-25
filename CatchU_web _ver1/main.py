#update
import random
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(50):
        man = random.randrange(1, 100)
        woman = random.randrange(1, 100)

        clothes_m = random.randrange(1, 100)
        devices_m = random.randrange(1, 100)
        perfume_m = random.randrange(1, 100)
        clothes_w = random.randrange(1, 100)
        devices_w = random.randrange(1, 100)
        perfume_w = random.randrange(1, 100)

        rate_clothes_m = clothes_m / (clothes_m+clothes_w)
        rate_clothes_w = clothes_w / (clothes_m + clothes_w)
        rate_clothes_m=int(round(rate_clothes_m,2)*100)
        rate_clothes_w = int(round(rate_clothes_w, 2)*100)

        rate_devices_m = devices_m / (devices_m + devices_w)
        rate_devices_w = devices_w / (devices_m + devices_w)
        rate_devices_m = int(round(rate_devices_m, 2)*100)
        rate_devices_w = int(round(rate_devices_w, 2)*100)

        rate_perfume_m = perfume_m / (perfume_m + perfume_w)
        rate_perfume_w = perfume_w / (perfume_m + perfume_w)
        rate_perfume_m = int(round(rate_perfume_m, 2)*100)
        rate_perfume_w = int(round(rate_perfume_w, 2)*100)


        print("1:::",man, woman)
        print("2:::",rate_clothes_m,rate_clothes_w ,rate_devices_m,rate_devices_w,rate_perfume_m,rate_perfume_w)

        f = open("countData.txt", "w")
        f.write(str(man) + '\n')
        f.write(str(woman))
        f.close()

        f2 = open("ratingData.txt", "w")
        # f2.write(str(rate_clothes_m)+' '+str(rate_clothes_w) + '\n')
        # f2.write(str(rate_devices_m) + ' ' + str(rate_devices_w) + '\n')
        # f2.write(str(rate_perfume_m) + ' ' + str(rate_perfume_w))
        f2.write(str(rate_clothes_m) + '\n')
        f2.write(str(rate_clothes_w) + '\n')
        f2.write(str(rate_devices_m) + '\n')
        f2.write(str(rate_devices_w) + '\n')
        f2.write(str(rate_perfume_m) + '\n')
        f2.write(str(rate_perfume_w) )


        f2.close()

        time.sleep(10)
