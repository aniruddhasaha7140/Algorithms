def main():
    s="abc"
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            substring=s[i:j]
            print(substring)
    return 

if __name__=="__main__":
    main()