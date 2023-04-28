function lexicoMaxSubsequence(s, n)
    {
        let st = [];

        // Stores if any alphabet is present
        // in the current stack
        let visited = new Array(26);
        let cnt = new Array(26);
        for (let i = 0; i < 26; i++) {
            visited[i] = 0;
            cnt[i] = 0;
        }

        console.log(visited, cnt)

        // Findthe number of occurrences of
        // the character s[i]
        for (let i = 0; i < n; i++) {
            cnt[s[i].charCodeAt() - 'a'.charCodeAt()]++;
        }

        console.log(cnt, 'count')
        console.log(visited, 'visited1')
        for (let i = 0; i < n; i++) {

            // Decrease the character count
            // in remaining string
            cnt[s[i].charCodeAt() - 'a'.charCodeAt()]--;

            // If character is already present
            // in the stack
            console.log(visited, 'visited?')
            if (visited[s[i].charCodeAt() - 'a'.charCodeAt()] > 0) {
                continue;
            }

            // if current character is greater
            // than last character in stack
            // then pop the top character
            while (st.length > 0 && st[st.length - 1].charCodeAt() < s[i].charCodeAt()
                   && cnt[st[st.length - 1].charCodeAt() - 'a'.charCodeAt()] != 0) {
                visited[st[st.length - 1].charCodeAt() - 'a'.charCodeAt()] = 0;
                st.pop();
            }

            // Push the current character
            st.push(s[i]);
            visited[s[i].charCodeAt() - 'a'.charCodeAt()] = 1;
        }

        // Stores the resultant string
        let s1 = "";

        // Generate the string
        while (st.length > 0) {
            s1 = st[st.length - 1] + s1;
            st.pop();
        }

        // Return the resultant string
        return s1;
    }

    let string = 'abacaba'

    console.log(lexicoMaxSubsequence(string,string.length ))
