shuxue = int(input('请输入数学成绩:'))
yuwen = int(input('请输入语文成绩:'))
if yuwen and shuxue >= 0 and yuwen and shuxue <= 100:
    if shuxue >= 60 and yuwen >= 60:
        if shuxue and yuwen >= 90 and shuxue and yuwen < 100:
            print('优秀肥肥,', end='')
        elif shuxue == 100 and yuwen < 100:
            print('厉害了，肥肥,数学%s,' % shuxue, end='')
        elif yuwen == 100 and shuxue < 100:
            print('厉害了，肥肥，语文%s' % yuwen, end='')
        elif shuxue == 100 and yuwen == 100:
            print('天神肥肥，语文%s' % yuwen, '数学%s' % shuxue, end='')
        else:
            print('继续加油吧，', end='')
        print('恭喜')
    elif shuxue or yuwen >= 60:
        if shuxue >= 60 and shuxue <= 90 and yuwen < 60:
            print('语文加油,', end='')
        elif yuwen >= 60 and yuwen <= 90 and shuxue < 60:
            print('数学加油,', end='')
        print('继续加油')
    elif shuxue and yuwen < 60 and shuxue >= 0 and yuwen >= 0:
        if shuxue == 0 and yuwen > 0:
            print('你没考数学？')
        elif yuwen == 0 and shuxue > 0:
            print('没考语文,这语文%s分？' % yuwen)
        elif shuxue == 0 and yuwen == 0:
            print('你都没考试？')
        print('渣渣')
else:
    print('请输入正确的成绩。')
