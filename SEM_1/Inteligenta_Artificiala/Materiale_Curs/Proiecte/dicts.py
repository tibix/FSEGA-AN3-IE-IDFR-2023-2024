def main():
    #citeste mbox-short.txt si ia liniile care incep cu From
    with open('mbox-short.txt') as f:
        lines = [ line for line in f if line.startswith("From") and len(line.split(' ')) > 2 ]

    mails_per_day = dict()

    for line in lines:
        words = line.split(' ')
        mails_per_day[words[2]] = mails_per_day.get(words[2], 0)+1

    print(mails_per_day)

    with open('mbox-short.txt') as f:
        lines = [ line for line in f if line.startswith("From") ]

    mails_per_account = dict()

    for line in lines:
        words = line.split(' ')
        mails_per_account[words[1].rstrip()] = mails_per_account.get(words[1].rstrip(), 0)+1

    print(mails_per_account)

if __name__ == "__main__":
    main()