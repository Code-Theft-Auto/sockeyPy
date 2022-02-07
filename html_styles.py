styles = [
  '''
  <!-- HTML generated using hilite.me --><div style="background: #272822; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #f92672">import</span> <span style="color: #f8f8f2">os</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">sys</span>

<span style="color: #f8f8f2">sys</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">path</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">insert(</span><span style="color: #ae81ff">1</span><span style="color: #f8f8f2">,</span> <span style="color: #e6db74">&#39;./modules&#39;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">json</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">pytz</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">asyncio</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">discord</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">datetime</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">keep_alive</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">youtube_dl</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">discord_slash</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">os</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">getenv</span>
<span style="color: #f92672">import</span> <span style="color: #f8f8f2">impfunctions</span> <span style="color: #f92672">as</span> <span style="color: #f8f8f2">func</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">keywords</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">KEYWORD</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">googlesearch</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">search</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">discord.ext</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">commands</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">youtube_dl</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">YoutubeDL</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">discord_slash</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">SlashCommand</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">discord_slash.model</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">ButtonStyle</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">discord_slash.utils.manage_components</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">create_button,</span> <span style="color: #f8f8f2">create_actionrow</span>
<span style="color: #f92672">from</span> <span style="color: #f8f8f2">discord_slash.utils.manage_components</span> <span style="color: #f92672">import</span> <span style="color: #f8f8f2">ComponentContext,</span> <span style="color: #f8f8f2">wait_for_component</span>

<span style="color: #f8f8f2">bot</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">commands</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">Bot(command_prefix</span><span style="color: #f92672">=</span><span style="color: #e6db74">&#39;.&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #f8f8f2">help_command</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">None)</span>

<span style="color: #f8f8f2">slash</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">SlashCommand(bot,</span>
                     <span style="color: #f8f8f2">sync_commands</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">True,</span>
                     <span style="color: #f8f8f2">sync_on_cog_reload</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">True,</span>
                     <span style="color: #f8f8f2">application_id</span><span style="color: #f92672">=</span><span style="color: #ae81ff">916685474364534805</span><span style="color: #f8f8f2">)</span>

<span style="color: #f8f8f2">beats_activity</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">[discord</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">ActivityType</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">listening,</span> <span style="color: #e6db74">&quot;Beats&quot;</span><span style="color: #f8f8f2">]</span>

<span style="color: #f8f8f2">extensions</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">[</span><span style="color: #e6db74">&quot;music&quot;</span><span style="color: #f8f8f2">,</span> <span style="color: #e6db74">&quot;general&quot;</span><span style="color: #f8f8f2">]</span>
<span style="color: #f8f8f2">bot</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">load_extension(</span><span style="color: #e6db74">&quot;music&quot;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f8f8f2">bot</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">load_extension(</span><span style="color: #e6db74">&quot;general&quot;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f8f8f2">bot</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">load_extension(</span><span style="color: #e6db74">&quot;slashcog&quot;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f8f8f2">IST</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">pytz</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">timezone(</span><span style="color: #e6db74">&#39;Asia/Kolkata&#39;</span><span style="color: #f8f8f2">)</span>


<span style="color: #a6e22e">@bot.event</span>
<span style="color: #75715e">#on ready</span>
<span style="color: #f8f8f2">async</span> <span style="color: #66d9ef">def</span> <span style="color: #a6e22e">on_ready</span><span style="color: #f8f8f2">():</span>
    <span style="color: #66d9ef">print</span><span style="color: #f8f8f2">(</span><span style="color: #e6db74">&quot;logged in as {0.user}&quot;</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">format(bot))</span>
    <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">bot</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">change_presence(activity</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">discord</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">Activity(</span>
        <span style="color: #f8f8f2">type</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">beats_activity[</span><span style="color: #ae81ff">0</span><span style="color: #f8f8f2">],</span> <span style="color: #f8f8f2">name</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">beats_activity[</span><span style="color: #ae81ff">1</span><span style="color: #f8f8f2">]),</span>
                              <span style="color: #f8f8f2">status</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">discord</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">Status</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">dnd)</span>


<span style="color: #a6e22e">@bot.event</span>
<span style="color: #f8f8f2">async</span> <span style="color: #66d9ef">def</span> <span style="color: #a6e22e">on_message</span><span style="color: #f8f8f2">(msg):</span>
    <span style="color: #66d9ef">if</span> <span style="color: #f8f8f2">(msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">bot):</span>
        <span style="color: #66d9ef">return</span>
    <span style="color: #f8f8f2">allstr</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">tuple(KEYWORD)</span>
    <span style="color: #f8f8f2">authid</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">str(msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">id)</span>
    <span style="color: #f8f8f2">authname</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span>
    <span style="color: #66d9ef">with</span> <span style="color: #f8f8f2">open(</span><span style="color: #e6db74">&quot;json.json&quot;</span><span style="color: #f8f8f2">,</span> <span style="color: #e6db74">&quot;r&quot;</span><span style="color: #f8f8f2">)</span> <span style="color: #66d9ef">as</span> <span style="color: #f8f8f2">jsonfile:</span>
        <span style="color: #f8f8f2">jsonfile</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">json</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">load(jsonfile)</span>
    <span style="color: #66d9ef">if</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">startswith(allstr):</span>

        <span style="color: #66d9ef">with</span> <span style="color: #f8f8f2">open(</span><span style="color: #e6db74">&quot;json.json&quot;</span><span style="color: #f8f8f2">,</span> <span style="color: #e6db74">&quot;w&quot;</span><span style="color: #f8f8f2">)</span> <span style="color: #66d9ef">as</span> <span style="color: #f8f8f2">f:</span>
            <span style="color: #66d9ef">if</span> <span style="color: #f8f8f2">authid</span> <span style="color: #f92672">in</span> <span style="color: #f8f8f2">jsonfile:</span>
                <span style="color: #f8f8f2">time_</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">datetime</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">datetime</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">now(IST)</span>
                <span style="color: #66d9ef">try</span><span style="color: #f8f8f2">:</span>
                    <span style="color: #f8f8f2">content</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                        <span style="color: #e6db74">&quot;message&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content,</span>
                        <span style="color: #e6db74">&quot;time&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">time_</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">strftime(</span><span style="color: #e6db74">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #f8f8f2">),</span>
                        <span style="color: #e6db74">&quot;guild&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">guild</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">name</span>
                    <span style="color: #f8f8f2">}</span>
                <span style="color: #66d9ef">except</span> <span style="color: #a6e22e">AttributeError</span><span style="color: #f8f8f2">:</span>
                    <span style="color: #f8f8f2">content</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                        <span style="color: #e6db74">&quot;message&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content,</span>
                        <span style="color: #e6db74">&quot;time&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">time_</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">strftime(</span><span style="color: #e6db74">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #f8f8f2">),</span>
                        <span style="color: #e6db74">&quot;guild&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #e6db74">&quot;DM&quot;</span>
                    <span style="color: #f8f8f2">}</span>

                <span style="color: #66d9ef">else</span><span style="color: #f8f8f2">:</span>
                    <span style="color: #f8f8f2">content</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                        <span style="color: #e6db74">&quot;message&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content,</span>
                        <span style="color: #e6db74">&quot;time&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">time_</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">strftime(</span><span style="color: #e6db74">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #f8f8f2">),</span>
                        <span style="color: #e6db74">&quot;guild&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">guild</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">name</span>
                    <span style="color: #f8f8f2">}</span>
                <span style="color: #f8f8f2">jsonfile[authid][</span><span style="color: #e6db74">&quot;messages&quot;</span><span style="color: #f8f8f2">]</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">append(content)</span>
                <span style="color: #f8f8f2">json</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">dump(jsonfile,</span> <span style="color: #f8f8f2">f,</span> <span style="color: #f8f8f2">indent</span><span style="color: #f92672">=</span><span style="color: #ae81ff">7</span><span style="color: #f8f8f2">)</span>
            <span style="color: #66d9ef">else</span><span style="color: #f8f8f2">:</span>
                <span style="color: #f8f8f2">time_</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">datetime</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">datetime</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">now(IST)</span>
                <span style="color: #f8f8f2">jsonfile[authid]</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                    <span style="color: #e6db74">&quot;id&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">int(authid),</span>
                    <span style="color: #e6db74">&quot;name&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">f</span><span style="color: #e6db74">&quot;{authname}&quot;</span><span style="color: #f8f8f2">,</span>
                    <span style="color: #e6db74">&quot;messages&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">[]</span>
                <span style="color: #f8f8f2">}</span>
                <span style="color: #66d9ef">try</span><span style="color: #f8f8f2">:</span>
                    <span style="color: #f8f8f2">content</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                        <span style="color: #e6db74">&quot;message&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content,</span>
                        <span style="color: #e6db74">&quot;time&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">time_</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">strftime(</span><span style="color: #e6db74">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #f8f8f2">),</span>
                        <span style="color: #e6db74">&quot;guild&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">guild</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">name</span>
                    <span style="color: #f8f8f2">}</span>
                <span style="color: #66d9ef">except</span> <span style="color: #a6e22e">AttributeError</span><span style="color: #f8f8f2">:</span>
                    <span style="color: #f8f8f2">content</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                        <span style="color: #e6db74">&quot;message&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content,</span>
                        <span style="color: #e6db74">&quot;time&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">time_</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">strftime(</span><span style="color: #e6db74">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #f8f8f2">),</span>
                        <span style="color: #e6db74">&quot;guild&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #e6db74">&quot;DM&quot;</span>
                    <span style="color: #f8f8f2">}</span>

                <span style="color: #66d9ef">else</span><span style="color: #f8f8f2">:</span>
                    <span style="color: #f8f8f2">content</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span>
                        <span style="color: #e6db74">&quot;message&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">content,</span>
                        <span style="color: #e6db74">&quot;time&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">time_</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">strftime(</span><span style="color: #e6db74">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #f8f8f2">),</span>
                        <span style="color: #e6db74">&quot;guild&quot;</span><span style="color: #f8f8f2">:</span> <span style="color: #f8f8f2">msg</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">guild</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">name</span>
                    <span style="color: #f8f8f2">}</span>
                <span style="color: #f8f8f2">jsonfile[authid][</span><span style="color: #e6db74">&quot;messages&quot;</span><span style="color: #f8f8f2">]</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">append(content)</span>
                <span style="color: #f8f8f2">json</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">dump(jsonfile,</span> <span style="color: #f8f8f2">f,</span> <span style="color: #f8f8f2">indent</span><span style="color: #f92672">=</span><span style="color: #ae81ff">7</span><span style="color: #f8f8f2">)</span>
    <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">bot</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">process_commands(msg)</span>


<span style="color: #a6e22e">@bot.command</span><span style="color: #f8f8f2">()</span>
<span style="color: #f8f8f2">async</span> <span style="color: #66d9ef">def</span> <span style="color: #a6e22e">gs</span><span style="color: #f8f8f2">(ctx,</span> <span style="color: #f8f8f2">query):</span>
    <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">ctx</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">send(f</span><span style="color: #e6db74">&quot;Here are the links related to your question!&quot;</span><span style="color: #f8f8f2">)</span>
    <span style="color: #66d9ef">for</span> <span style="color: #f8f8f2">j</span> <span style="color: #f92672">in</span> <span style="color: #f8f8f2">search(query,</span> <span style="color: #f8f8f2">safe</span><span style="color: #f92672">=</span><span style="color: #e6db74">&#39;on&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #f8f8f2">start</span><span style="color: #f92672">=</span><span style="color: #ae81ff">1</span><span style="color: #f8f8f2">,</span> <span style="color: #f8f8f2">stop</span><span style="color: #f92672">=</span><span style="color: #ae81ff">1</span><span style="color: #f8f8f2">):</span>
        <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">ctx</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">send(f</span><span style="color: #e6db74">&quot;</span><span style="color: #ae81ff">\n</span><span style="color: #e6db74">:point_right: {j}&quot;</span><span style="color: #f8f8f2">)</span>
        <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">ctx</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">author</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">send(</span>
            <span style="color: #e6db74">&quot;Have any more questions:question:</span><span style="color: #ae81ff">\n</span><span style="color: #e6db74">Feel free to ask again :smiley: !&quot;</span>
        <span style="color: #f8f8f2">)</span>


<span style="color: #f8f8f2">NEXTBUTTON</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">[</span>
    <span style="color: #f8f8f2">create_button(ButtonStyle</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">green,</span> <span style="color: #f8f8f2">label</span><span style="color: #f92672">=</span><span style="color: #e6db74">&quot;Next&quot;</span><span style="color: #f8f8f2">,</span> <span style="color: #f8f8f2">custom_id</span><span style="color: #f92672">=</span><span style="color: #e6db74">&quot;NextMeme&quot;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f8f8f2">]</span>


<span style="color: #a6e22e">@bot.command</span><span style="color: #f8f8f2">(name</span><span style="color: #f92672">=</span><span style="color: #e6db74">&quot;meme&quot;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f8f8f2">async</span> <span style="color: #66d9ef">def</span> <span style="color: #a6e22e">meme_</span><span style="color: #f8f8f2">(ctx):</span>
    <span style="color: #f8f8f2">em</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">func</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">meme()</span>
    <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">ctx</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">send(embed</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">em,</span> <span style="color: #f8f8f2">components</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">[create_actionrow(</span><span style="color: #f92672">*</span><span style="color: #f8f8f2">NEXTBUTTON)])</span>

    <span style="color: #66d9ef">while</span> <span style="color: #ae81ff">1</span><span style="color: #f8f8f2">:</span>
        <span style="color: #66d9ef">try</span><span style="color: #f8f8f2">:</span>
            <span style="color: #f8f8f2">button_ctx:</span> <span style="color: #f8f8f2">ComponentContext</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">wait_for_component(</span>
                <span style="color: #f8f8f2">bot,</span> <span style="color: #f8f8f2">components</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">NEXTBUTTON,</span> <span style="color: #f8f8f2">timeout</span><span style="color: #f92672">=</span><span style="color: #ae81ff">10</span><span style="color: #f8f8f2">)</span>
            <span style="color: #f8f8f2">await</span> <span style="color: #f8f8f2">button_ctx</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">edit_origin(embed</span><span style="color: #f92672">=</span><span style="color: #f8f8f2">func</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">meme())</span>
        <span style="color: #66d9ef">except</span> <span style="color: #f8f8f2">asyncio</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">exceptions</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">TimeoutError:</span>
            <span style="color: #66d9ef">break</span>


<span style="color: #f8f8f2">TOKEN</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">os</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">getenv(</span><span style="color: #e6db74">&quot;TOKEN&quot;</span><span style="color: #f8f8f2">)</span>
<span style="color: #f8f8f2">keep_alive</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">keep_alive()</span>
<span style="color: #f8f8f2">bot</span><span style="color: #f92672">.</span><span style="color: #f8f8f2">run(TOKEN)</span>  <span style="color: #75715e"># client login</span>
</pre></td></tr></table></div>

  ''',
  '''
  <!-- HTML generated using hilite.me --><div style="background: #111111; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">os</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">sys</span>

<span style="color: #ffffff">sys.path.insert(</span><span style="color: #0086f7; font-weight: bold">1</span><span style="color: #ffffff">,</span> <span style="color: #0086d2">&#39;./modules&#39;</span><span style="color: #ffffff">)</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">json</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">pytz</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">asyncio</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">discord</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">datetime</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">keep_alive</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">youtube_dl</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">discord_slash</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">os</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">getenv</span>
<span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">impfunctions</span> <span style="color: #fb660a; font-weight: bold">as</span> <span style="color: #ffffff">func</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">keywords</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">KEYWORD</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">googlesearch</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">search</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">discord.ext</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">commands</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">youtube_dl</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">YoutubeDL</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">discord_slash</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">SlashCommand</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">discord_slash.model</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">ButtonStyle</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">discord_slash.utils.manage_components</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">create_button,</span> <span style="color: #ffffff">create_actionrow</span>
<span style="color: #fb660a; font-weight: bold">from</span> <span style="color: #ffffff">discord_slash.utils.manage_components</span> <span style="color: #fb660a; font-weight: bold">import</span> <span style="color: #ffffff">ComponentContext,</span> <span style="color: #ffffff">wait_for_component</span>

<span style="color: #ffffff">bot</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">commands.Bot(command_prefix=</span><span style="color: #0086d2">&#39;.&#39;</span><span style="color: #ffffff">,</span> <span style="color: #ffffff">help_command=None)</span>

<span style="color: #ffffff">slash</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">SlashCommand(bot,</span>
                     <span style="color: #ffffff">sync_commands=True,</span>
                     <span style="color: #ffffff">sync_on_cog_reload=True,</span>
                     <span style="color: #ffffff">application_id=</span><span style="color: #0086f7; font-weight: bold">916685474364534805</span><span style="color: #ffffff">)</span>

<span style="color: #ffffff">beats_activity</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">[discord.ActivityType.listening,</span> <span style="color: #0086d2">&quot;Beats&quot;</span><span style="color: #ffffff">]</span>

<span style="color: #ffffff">extensions</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">[</span><span style="color: #0086d2">&quot;music&quot;</span><span style="color: #ffffff">,</span> <span style="color: #0086d2">&quot;general&quot;</span><span style="color: #ffffff">]</span>
<span style="color: #ffffff">bot.load_extension(</span><span style="color: #0086d2">&quot;music&quot;</span><span style="color: #ffffff">)</span>
<span style="color: #ffffff">bot.load_extension(</span><span style="color: #0086d2">&quot;general&quot;</span><span style="color: #ffffff">)</span>
<span style="color: #ffffff">bot.load_extension(</span><span style="color: #0086d2">&quot;slashcog&quot;</span><span style="color: #ffffff">)</span>
<span style="color: #ffffff">IST</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">pytz.timezone(</span><span style="color: #0086d2">&#39;Asia/Kolkata&#39;</span><span style="color: #ffffff">)</span>


<span style="color: #ffffff">@bot.event</span>
<span style="color: #008800; font-style: italic; background-color: #0f140f">#on ready</span>
<span style="color: #ffffff">async</span> <span style="color: #fb660a; font-weight: bold">def</span> <span style="color: #ff0086; font-weight: bold">on_ready</span><span style="color: #ffffff">():</span>
    <span style="color: #fb660a; font-weight: bold">print</span><span style="color: #ffffff">(</span><span style="color: #0086d2">&quot;logged in as {0.user}&quot;</span><span style="color: #ffffff">.format(bot))</span>
    <span style="color: #ffffff">await</span> <span style="color: #ffffff">bot.change_presence(activity=discord.Activity(</span>
        <span style="color: #ffffff">type=beats_activity[</span><span style="color: #0086f7; font-weight: bold">0</span><span style="color: #ffffff">],</span> <span style="color: #ffffff">name=beats_activity[</span><span style="color: #0086f7; font-weight: bold">1</span><span style="color: #ffffff">]),</span>
                              <span style="color: #ffffff">status=discord.Status.dnd)</span>


<span style="color: #ffffff">@bot.event</span>
<span style="color: #ffffff">async</span> <span style="color: #fb660a; font-weight: bold">def</span> <span style="color: #ff0086; font-weight: bold">on_message</span><span style="color: #ffffff">(msg):</span>
    <span style="color: #fb660a; font-weight: bold">if</span> <span style="color: #ffffff">(msg.author.bot):</span>
        <span style="color: #fb660a; font-weight: bold">return</span>
    <span style="color: #ffffff">allstr</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">tuple(KEYWORD)</span>
    <span style="color: #ffffff">authid</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">str(msg.author.id)</span>
    <span style="color: #ffffff">authname</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">msg.author</span>
    <span style="color: #fb660a; font-weight: bold">with</span> <span style="color: #ffffff">open(</span><span style="color: #0086d2">&quot;json.json&quot;</span><span style="color: #ffffff">,</span> <span style="color: #0086d2">&quot;r&quot;</span><span style="color: #ffffff">)</span> <span style="color: #fb660a; font-weight: bold">as</span> <span style="color: #ffffff">jsonfile:</span>
        <span style="color: #ffffff">jsonfile</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">json.load(jsonfile)</span>
    <span style="color: #fb660a; font-weight: bold">if</span> <span style="color: #ffffff">msg.content.startswith(allstr):</span>

        <span style="color: #fb660a; font-weight: bold">with</span> <span style="color: #ffffff">open(</span><span style="color: #0086d2">&quot;json.json&quot;</span><span style="color: #ffffff">,</span> <span style="color: #0086d2">&quot;w&quot;</span><span style="color: #ffffff">)</span> <span style="color: #fb660a; font-weight: bold">as</span> <span style="color: #ffffff">f:</span>
            <span style="color: #fb660a; font-weight: bold">if</span> <span style="color: #ffffff">authid</span> <span style="color: #ffffff">in</span> <span style="color: #ffffff">jsonfile:</span>
                <span style="color: #ffffff">time_</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">datetime.datetime.now(IST)</span>
                <span style="color: #fb660a; font-weight: bold">try</span><span style="color: #ffffff">:</span>
                    <span style="color: #ffffff">content</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                        <span style="color: #0086d2">&quot;message&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.content,</span>
                        <span style="color: #0086d2">&quot;time&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">time_.strftime(</span><span style="color: #0086d2">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #ffffff">),</span>
                        <span style="color: #0086d2">&quot;guild&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.author.guild.name</span>
                    <span style="color: #ffffff">}</span>
                <span style="color: #fb660a; font-weight: bold">except</span> <span style="color: #ffffff">AttributeError:</span>
                    <span style="color: #ffffff">content</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                        <span style="color: #0086d2">&quot;message&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.content,</span>
                        <span style="color: #0086d2">&quot;time&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">time_.strftime(</span><span style="color: #0086d2">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #ffffff">),</span>
                        <span style="color: #0086d2">&quot;guild&quot;</span><span style="color: #ffffff">:</span> <span style="color: #0086d2">&quot;DM&quot;</span>
                    <span style="color: #ffffff">}</span>

                <span style="color: #fb660a; font-weight: bold">else</span><span style="color: #ffffff">:</span>
                    <span style="color: #ffffff">content</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                        <span style="color: #0086d2">&quot;message&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.content,</span>
                        <span style="color: #0086d2">&quot;time&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">time_.strftime(</span><span style="color: #0086d2">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #ffffff">),</span>
                        <span style="color: #0086d2">&quot;guild&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.author.guild.name</span>
                    <span style="color: #ffffff">}</span>
                <span style="color: #ffffff">jsonfile[authid][</span><span style="color: #0086d2">&quot;messages&quot;</span><span style="color: #ffffff">].append(content)</span>
                <span style="color: #ffffff">json.dump(jsonfile,</span> <span style="color: #ffffff">f,</span> <span style="color: #ffffff">indent=</span><span style="color: #0086f7; font-weight: bold">7</span><span style="color: #ffffff">)</span>
            <span style="color: #fb660a; font-weight: bold">else</span><span style="color: #ffffff">:</span>
                <span style="color: #ffffff">time_</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">datetime.datetime.now(IST)</span>
                <span style="color: #ffffff">jsonfile[authid]</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                    <span style="color: #0086d2">&quot;id&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">int(authid),</span>
                    <span style="color: #0086d2">&quot;name&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">f</span><span style="color: #0086d2">&quot;{authname}&quot;</span><span style="color: #ffffff">,</span>
                    <span style="color: #0086d2">&quot;messages&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">[]</span>
                <span style="color: #ffffff">}</span>
                <span style="color: #fb660a; font-weight: bold">try</span><span style="color: #ffffff">:</span>
                    <span style="color: #ffffff">content</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                        <span style="color: #0086d2">&quot;message&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.content,</span>
                        <span style="color: #0086d2">&quot;time&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">time_.strftime(</span><span style="color: #0086d2">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #ffffff">),</span>
                        <span style="color: #0086d2">&quot;guild&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.author.guild.name</span>
                    <span style="color: #ffffff">}</span>
                <span style="color: #fb660a; font-weight: bold">except</span> <span style="color: #ffffff">AttributeError:</span>
                    <span style="color: #ffffff">content</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                        <span style="color: #0086d2">&quot;message&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.content,</span>
                        <span style="color: #0086d2">&quot;time&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">time_.strftime(</span><span style="color: #0086d2">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #ffffff">),</span>
                        <span style="color: #0086d2">&quot;guild&quot;</span><span style="color: #ffffff">:</span> <span style="color: #0086d2">&quot;DM&quot;</span>
                    <span style="color: #ffffff">}</span>

                <span style="color: #fb660a; font-weight: bold">else</span><span style="color: #ffffff">:</span>
                    <span style="color: #ffffff">content</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">{</span>
                        <span style="color: #0086d2">&quot;message&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.content,</span>
                        <span style="color: #0086d2">&quot;time&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">time_.strftime(</span><span style="color: #0086d2">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #ffffff">),</span>
                        <span style="color: #0086d2">&quot;guild&quot;</span><span style="color: #ffffff">:</span> <span style="color: #ffffff">msg.author.guild.name</span>
                    <span style="color: #ffffff">}</span>
                <span style="color: #ffffff">jsonfile[authid][</span><span style="color: #0086d2">&quot;messages&quot;</span><span style="color: #ffffff">].append(content)</span>
                <span style="color: #ffffff">json.dump(jsonfile,</span> <span style="color: #ffffff">f,</span> <span style="color: #ffffff">indent=</span><span style="color: #0086f7; font-weight: bold">7</span><span style="color: #ffffff">)</span>
    <span style="color: #ffffff">await</span> <span style="color: #ffffff">bot.process_commands(msg)</span>


<span style="color: #ffffff">@bot.command()</span>
<span style="color: #ffffff">async</span> <span style="color: #fb660a; font-weight: bold">def</span> <span style="color: #ff0086; font-weight: bold">gs</span><span style="color: #ffffff">(ctx,</span> <span style="color: #ffffff">query):</span>
    <span style="color: #ffffff">await</span> <span style="color: #ffffff">ctx.author.send(f</span><span style="color: #0086d2">&quot;Here are the links related to your question!&quot;</span><span style="color: #ffffff">)</span>
    <span style="color: #fb660a; font-weight: bold">for</span> <span style="color: #ffffff">j</span> <span style="color: #ffffff">in</span> <span style="color: #ffffff">search(query,</span> <span style="color: #ffffff">safe=</span><span style="color: #0086d2">&#39;on&#39;</span><span style="color: #ffffff">,</span> <span style="color: #ffffff">start=</span><span style="color: #0086f7; font-weight: bold">1</span><span style="color: #ffffff">,</span> <span style="color: #ffffff">stop=</span><span style="color: #0086f7; font-weight: bold">1</span><span style="color: #ffffff">):</span>
        <span style="color: #ffffff">await</span> <span style="color: #ffffff">ctx.author.send(f</span><span style="color: #0086d2">&quot;\n:point_right: {j}&quot;</span><span style="color: #ffffff">)</span>
        <span style="color: #ffffff">await</span> <span style="color: #ffffff">ctx.author.send(</span>
            <span style="color: #0086d2">&quot;Have any more questions:question:\nFeel free to ask again :smiley: !&quot;</span>
        <span style="color: #ffffff">)</span>


<span style="color: #ffffff">NEXTBUTTON</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">[</span>
    <span style="color: #ffffff">create_button(ButtonStyle.green,</span> <span style="color: #ffffff">label=</span><span style="color: #0086d2">&quot;Next&quot;</span><span style="color: #ffffff">,</span> <span style="color: #ffffff">custom_id=</span><span style="color: #0086d2">&quot;NextMeme&quot;</span><span style="color: #ffffff">)</span>
<span style="color: #ffffff">]</span>


<span style="color: #ffffff">@bot.command(name=</span><span style="color: #0086d2">&quot;meme&quot;</span><span style="color: #ffffff">)</span>
<span style="color: #ffffff">async</span> <span style="color: #fb660a; font-weight: bold">def</span> <span style="color: #ff0086; font-weight: bold">meme_</span><span style="color: #ffffff">(ctx):</span>
    <span style="color: #ffffff">em</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">func.meme()</span>
    <span style="color: #ffffff">await</span> <span style="color: #ffffff">ctx.send(embed=em,</span> <span style="color: #ffffff">components=[create_actionrow(*NEXTBUTTON)])</span>

    <span style="color: #fb660a; font-weight: bold">while</span> <span style="color: #0086f7; font-weight: bold">1</span><span style="color: #ffffff">:</span>
        <span style="color: #fb660a; font-weight: bold">try</span><span style="color: #ffffff">:</span>
            <span style="color: #ffffff">button_ctx:</span> <span style="color: #ffffff">ComponentContext</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">await</span> <span style="color: #ffffff">wait_for_component(</span>
                <span style="color: #ffffff">bot,</span> <span style="color: #ffffff">components=NEXTBUTTON,</span> <span style="color: #ffffff">timeout=</span><span style="color: #0086f7; font-weight: bold">10</span><span style="color: #ffffff">)</span>
            <span style="color: #ffffff">await</span> <span style="color: #ffffff">button_ctx.edit_origin(embed=func.meme())</span>
        <span style="color: #fb660a; font-weight: bold">except</span> <span style="color: #ffffff">asyncio.exceptions.TimeoutError:</span>
            <span style="color: #fb660a; font-weight: bold">break</span>


<span style="color: #ffffff">TOKEN</span> <span style="color: #ffffff">=</span> <span style="color: #ffffff">os.getenv(</span><span style="color: #0086d2">&quot;TOKEN&quot;</span><span style="color: #ffffff">)</span>
<span style="color: #ffffff">keep_alive.keep_alive()</span>
<span style="color: #ffffff">bot.run(TOKEN)</span>  <span style="color: #008800; font-style: italic; background-color: #0f140f"># client login</span>
</pre></td></tr></table></div>

''',
'''
<!-- HTML generated using hilite.me --><div style="background: #202020; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">os</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">sys</span>

<span style="color: #d0d0d0">sys.path.insert(</span><span style="color: #3677a9">1</span><span style="color: #d0d0d0">,</span> <span style="color: #ed9d13">&#39;./modules&#39;</span><span style="color: #d0d0d0">)</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">json</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">pytz</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">asyncio</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">discord</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">datetime</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">keep_alive</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">youtube_dl</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">discord_slash</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">os</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">getenv</span>
<span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #447fcf; text-decoration: underline">impfunctions</span> <span style="color: #6ab825; font-weight: bold">as</span> <span style="color: #447fcf; text-decoration: underline">func</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">keywords</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">KEYWORD</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">googlesearch</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">search</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">discord.ext</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">commands</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">youtube_dl</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">YoutubeDL</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">discord_slash</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">SlashCommand</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">discord_slash.model</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">ButtonStyle</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">discord_slash.utils.manage_components</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">create_button,</span> <span style="color: #d0d0d0">create_actionrow</span>
<span style="color: #6ab825; font-weight: bold">from</span> <span style="color: #447fcf; text-decoration: underline">discord_slash.utils.manage_components</span> <span style="color: #6ab825; font-weight: bold">import</span> <span style="color: #d0d0d0">ComponentContext,</span> <span style="color: #d0d0d0">wait_for_component</span>

<span style="color: #d0d0d0">bot</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">commands.Bot(command_prefix=</span><span style="color: #ed9d13">&#39;.&#39;</span><span style="color: #d0d0d0">,</span> <span style="color: #d0d0d0">help_command=</span><span style="color: #24909d">None</span><span style="color: #d0d0d0">)</span>

<span style="color: #d0d0d0">slash</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">SlashCommand(bot,</span>
                     <span style="color: #d0d0d0">sync_commands=</span><span style="color: #24909d">True</span><span style="color: #d0d0d0">,</span>
                     <span style="color: #d0d0d0">sync_on_cog_reload=</span><span style="color: #24909d">True</span><span style="color: #d0d0d0">,</span>
                     <span style="color: #d0d0d0">application_id=</span><span style="color: #3677a9">916685474364534805</span><span style="color: #d0d0d0">)</span>

<span style="color: #d0d0d0">beats_activity</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">[discord.ActivityType.listening,</span> <span style="color: #ed9d13">&quot;Beats&quot;</span><span style="color: #d0d0d0">]</span>

<span style="color: #d0d0d0">extensions</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">[</span><span style="color: #ed9d13">&quot;music&quot;</span><span style="color: #d0d0d0">,</span> <span style="color: #ed9d13">&quot;general&quot;</span><span style="color: #d0d0d0">]</span>
<span style="color: #d0d0d0">bot.load_extension(</span><span style="color: #ed9d13">&quot;music&quot;</span><span style="color: #d0d0d0">)</span>
<span style="color: #d0d0d0">bot.load_extension(</span><span style="color: #ed9d13">&quot;general&quot;</span><span style="color: #d0d0d0">)</span>
<span style="color: #d0d0d0">bot.load_extension(</span><span style="color: #ed9d13">&quot;slashcog&quot;</span><span style="color: #d0d0d0">)</span>
<span style="color: #d0d0d0">IST</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">pytz.timezone(</span><span style="color: #ed9d13">&#39;Asia/Kolkata&#39;</span><span style="color: #d0d0d0">)</span>


<span style="color: #ffa500">@bot.event</span>
<span style="color: #999999; font-style: italic">#on ready</span>
<span style="color: #d0d0d0">async</span> <span style="color: #6ab825; font-weight: bold">def</span> <span style="color: #447fcf">on_ready</span><span style="color: #d0d0d0">():</span>
    <span style="color: #6ab825; font-weight: bold">print</span><span style="color: #d0d0d0">(</span><span style="color: #ed9d13">&quot;logged in as {0.user}&quot;</span><span style="color: #d0d0d0">.format(bot))</span>
    <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">bot.change_presence(activity=discord.Activity(</span>
        <span style="color: #24909d">type</span><span style="color: #d0d0d0">=beats_activity[</span><span style="color: #3677a9">0</span><span style="color: #d0d0d0">],</span> <span style="color: #d0d0d0">name=beats_activity[</span><span style="color: #3677a9">1</span><span style="color: #d0d0d0">]),</span>
                              <span style="color: #d0d0d0">status=discord.Status.dnd)</span>


<span style="color: #ffa500">@bot.event</span>
<span style="color: #d0d0d0">async</span> <span style="color: #6ab825; font-weight: bold">def</span> <span style="color: #447fcf">on_message</span><span style="color: #d0d0d0">(msg):</span>
    <span style="color: #6ab825; font-weight: bold">if</span> <span style="color: #d0d0d0">(msg.author.bot):</span>
        <span style="color: #6ab825; font-weight: bold">return</span>
    <span style="color: #d0d0d0">allstr</span> <span style="color: #d0d0d0">=</span> <span style="color: #24909d">tuple</span><span style="color: #d0d0d0">(KEYWORD)</span>
    <span style="color: #d0d0d0">authid</span> <span style="color: #d0d0d0">=</span> <span style="color: #24909d">str</span><span style="color: #d0d0d0">(msg.author.id)</span>
    <span style="color: #d0d0d0">authname</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">msg.author</span>
    <span style="color: #6ab825; font-weight: bold">with</span> <span style="color: #24909d">open</span><span style="color: #d0d0d0">(</span><span style="color: #ed9d13">&quot;json.json&quot;</span><span style="color: #d0d0d0">,</span> <span style="color: #ed9d13">&quot;r&quot;</span><span style="color: #d0d0d0">)</span> <span style="color: #6ab825; font-weight: bold">as</span> <span style="color: #d0d0d0">jsonfile:</span>
        <span style="color: #d0d0d0">jsonfile</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">json.load(jsonfile)</span>
    <span style="color: #6ab825; font-weight: bold">if</span> <span style="color: #d0d0d0">msg.content.startswith(allstr):</span>

        <span style="color: #6ab825; font-weight: bold">with</span> <span style="color: #24909d">open</span><span style="color: #d0d0d0">(</span><span style="color: #ed9d13">&quot;json.json&quot;</span><span style="color: #d0d0d0">,</span> <span style="color: #ed9d13">&quot;w&quot;</span><span style="color: #d0d0d0">)</span> <span style="color: #6ab825; font-weight: bold">as</span> <span style="color: #d0d0d0">f:</span>
            <span style="color: #6ab825; font-weight: bold">if</span> <span style="color: #d0d0d0">authid</span> <span style="color: #6ab825; font-weight: bold">in</span> <span style="color: #d0d0d0">jsonfile:</span>
                <span style="color: #d0d0d0">time_</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">datetime.datetime.now(IST)</span>
                <span style="color: #6ab825; font-weight: bold">try</span><span style="color: #d0d0d0">:</span>
                    <span style="color: #d0d0d0">content</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                        <span style="color: #ed9d13">&quot;message&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.content,</span>
                        <span style="color: #ed9d13">&quot;time&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">time_.strftime(</span><span style="color: #ed9d13">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #d0d0d0">),</span>
                        <span style="color: #ed9d13">&quot;guild&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.author.guild.name</span>
                    <span style="color: #d0d0d0">}</span>
                <span style="color: #6ab825; font-weight: bold">except</span> <span style="color: #bbbbbb">AttributeError</span><span style="color: #d0d0d0">:</span>
                    <span style="color: #d0d0d0">content</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                        <span style="color: #ed9d13">&quot;message&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.content,</span>
                        <span style="color: #ed9d13">&quot;time&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">time_.strftime(</span><span style="color: #ed9d13">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #d0d0d0">),</span>
                        <span style="color: #ed9d13">&quot;guild&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #ed9d13">&quot;DM&quot;</span>
                    <span style="color: #d0d0d0">}</span>

                <span style="color: #6ab825; font-weight: bold">else</span><span style="color: #d0d0d0">:</span>
                    <span style="color: #d0d0d0">content</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                        <span style="color: #ed9d13">&quot;message&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.content,</span>
                        <span style="color: #ed9d13">&quot;time&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">time_.strftime(</span><span style="color: #ed9d13">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #d0d0d0">),</span>
                        <span style="color: #ed9d13">&quot;guild&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.author.guild.name</span>
                    <span style="color: #d0d0d0">}</span>
                <span style="color: #d0d0d0">jsonfile[authid][</span><span style="color: #ed9d13">&quot;messages&quot;</span><span style="color: #d0d0d0">].append(content)</span>
                <span style="color: #d0d0d0">json.dump(jsonfile,</span> <span style="color: #d0d0d0">f,</span> <span style="color: #d0d0d0">indent=</span><span style="color: #3677a9">7</span><span style="color: #d0d0d0">)</span>
            <span style="color: #6ab825; font-weight: bold">else</span><span style="color: #d0d0d0">:</span>
                <span style="color: #d0d0d0">time_</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">datetime.datetime.now(IST)</span>
                <span style="color: #d0d0d0">jsonfile[authid]</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                    <span style="color: #ed9d13">&quot;id&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #24909d">int</span><span style="color: #d0d0d0">(authid),</span>
                    <span style="color: #ed9d13">&quot;name&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">f</span><span style="color: #ed9d13">&quot;{authname}&quot;</span><span style="color: #d0d0d0">,</span>
                    <span style="color: #ed9d13">&quot;messages&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">[]</span>
                <span style="color: #d0d0d0">}</span>
                <span style="color: #6ab825; font-weight: bold">try</span><span style="color: #d0d0d0">:</span>
                    <span style="color: #d0d0d0">content</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                        <span style="color: #ed9d13">&quot;message&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.content,</span>
                        <span style="color: #ed9d13">&quot;time&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">time_.strftime(</span><span style="color: #ed9d13">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #d0d0d0">),</span>
                        <span style="color: #ed9d13">&quot;guild&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.author.guild.name</span>
                    <span style="color: #d0d0d0">}</span>
                <span style="color: #6ab825; font-weight: bold">except</span> <span style="color: #bbbbbb">AttributeError</span><span style="color: #d0d0d0">:</span>
                    <span style="color: #d0d0d0">content</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                        <span style="color: #ed9d13">&quot;message&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.content,</span>
                        <span style="color: #ed9d13">&quot;time&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">time_.strftime(</span><span style="color: #ed9d13">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #d0d0d0">),</span>
                        <span style="color: #ed9d13">&quot;guild&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #ed9d13">&quot;DM&quot;</span>
                    <span style="color: #d0d0d0">}</span>

                <span style="color: #6ab825; font-weight: bold">else</span><span style="color: #d0d0d0">:</span>
                    <span style="color: #d0d0d0">content</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">{</span>
                        <span style="color: #ed9d13">&quot;message&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.content,</span>
                        <span style="color: #ed9d13">&quot;time&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">time_.strftime(</span><span style="color: #ed9d13">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #d0d0d0">),</span>
                        <span style="color: #ed9d13">&quot;guild&quot;</span><span style="color: #d0d0d0">:</span> <span style="color: #d0d0d0">msg.author.guild.name</span>
                    <span style="color: #d0d0d0">}</span>
                <span style="color: #d0d0d0">jsonfile[authid][</span><span style="color: #ed9d13">&quot;messages&quot;</span><span style="color: #d0d0d0">].append(content)</span>
                <span style="color: #d0d0d0">json.dump(jsonfile,</span> <span style="color: #d0d0d0">f,</span> <span style="color: #d0d0d0">indent=</span><span style="color: #3677a9">7</span><span style="color: #d0d0d0">)</span>
    <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">bot.process_commands(msg)</span>


<span style="color: #ffa500">@bot.command</span><span style="color: #d0d0d0">()</span>
<span style="color: #d0d0d0">async</span> <span style="color: #6ab825; font-weight: bold">def</span> <span style="color: #447fcf">gs</span><span style="color: #d0d0d0">(ctx,</span> <span style="color: #d0d0d0">query):</span>
    <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">ctx.author.send(f</span><span style="color: #ed9d13">&quot;Here are the links related to your question!&quot;</span><span style="color: #d0d0d0">)</span>
    <span style="color: #6ab825; font-weight: bold">for</span> <span style="color: #d0d0d0">j</span> <span style="color: #6ab825; font-weight: bold">in</span> <span style="color: #d0d0d0">search(query,</span> <span style="color: #d0d0d0">safe=</span><span style="color: #ed9d13">&#39;on&#39;</span><span style="color: #d0d0d0">,</span> <span style="color: #d0d0d0">start=</span><span style="color: #3677a9">1</span><span style="color: #d0d0d0">,</span> <span style="color: #d0d0d0">stop=</span><span style="color: #3677a9">1</span><span style="color: #d0d0d0">):</span>
        <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">ctx.author.send(f</span><span style="color: #ed9d13">&quot;\n:point_right: {j}&quot;</span><span style="color: #d0d0d0">)</span>
        <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">ctx.author.send(</span>
            <span style="color: #ed9d13">&quot;Have any more questions:question:\nFeel free to ask again :smiley: !&quot;</span>
        <span style="color: #d0d0d0">)</span>


<span style="color: #d0d0d0">NEXTBUTTON</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">[</span>
    <span style="color: #d0d0d0">create_button(ButtonStyle.green,</span> <span style="color: #d0d0d0">label=</span><span style="color: #ed9d13">&quot;Next&quot;</span><span style="color: #d0d0d0">,</span> <span style="color: #d0d0d0">custom_id=</span><span style="color: #ed9d13">&quot;NextMeme&quot;</span><span style="color: #d0d0d0">)</span>
<span style="color: #d0d0d0">]</span>


<span style="color: #ffa500">@bot.command</span><span style="color: #d0d0d0">(name=</span><span style="color: #ed9d13">&quot;meme&quot;</span><span style="color: #d0d0d0">)</span>
<span style="color: #d0d0d0">async</span> <span style="color: #6ab825; font-weight: bold">def</span> <span style="color: #447fcf">meme_</span><span style="color: #d0d0d0">(ctx):</span>
    <span style="color: #d0d0d0">em</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">func.meme()</span>
    <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">ctx.send(embed=em,</span> <span style="color: #d0d0d0">components=[create_actionrow(*NEXTBUTTON)])</span>

    <span style="color: #6ab825; font-weight: bold">while</span> <span style="color: #3677a9">1</span><span style="color: #d0d0d0">:</span>
        <span style="color: #6ab825; font-weight: bold">try</span><span style="color: #d0d0d0">:</span>
            <span style="color: #d0d0d0">button_ctx:</span> <span style="color: #d0d0d0">ComponentContext</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">wait_for_component(</span>
                <span style="color: #d0d0d0">bot,</span> <span style="color: #d0d0d0">components=NEXTBUTTON,</span> <span style="color: #d0d0d0">timeout=</span><span style="color: #3677a9">10</span><span style="color: #d0d0d0">)</span>
            <span style="color: #d0d0d0">await</span> <span style="color: #d0d0d0">button_ctx.edit_origin(embed=func.meme())</span>
        <span style="color: #6ab825; font-weight: bold">except</span> <span style="color: #d0d0d0">asyncio.exceptions.TimeoutError:</span>
            <span style="color: #6ab825; font-weight: bold">break</span>


<span style="color: #d0d0d0">TOKEN</span> <span style="color: #d0d0d0">=</span> <span style="color: #d0d0d0">os.getenv(</span><span style="color: #ed9d13">&quot;TOKEN&quot;</span><span style="color: #d0d0d0">)</span>
<span style="color: #d0d0d0">keep_alive.keep_alive()</span>
<span style="color: #d0d0d0">bot.run(TOKEN)</span>  <span style="color: #999999; font-style: italic"># client login</span>
</pre></td></tr></table></div>

''',
'''
<!-- HTML generated using hilite.me --><div style="background: #000000; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #ff0000">import</span> os
<span style="color: #ff0000">import</span> sys

sys.path.insert(1, <span style="color: #87ceeb">&#39;./modules&#39;</span>)
<span style="color: #ff0000">import</span> json
<span style="color: #ff0000">import</span> pytz
<span style="color: #ff0000">import</span> asyncio
<span style="color: #ff0000">import</span> discord
<span style="color: #ff0000">import</span> datetime
<span style="color: #ff0000">import</span> keep_alive
<span style="color: #ff0000">import</span> youtube_dl
<span style="color: #ff0000">import</span> discord_slash
<span style="color: #ff0000">from</span> os <span style="color: #ff0000">import</span> getenv
<span style="color: #ff0000">import</span> impfunctions <span style="color: #ff0000">as</span> func
<span style="color: #ff0000">from</span> keywords <span style="color: #ff0000">import</span> KEYWORD
<span style="color: #ff0000">from</span> googlesearch <span style="color: #ff0000">import</span> search
<span style="color: #ff0000">from</span> discord.ext <span style="color: #ff0000">import</span> commands
<span style="color: #ff0000">from</span> youtube_dl <span style="color: #ff0000">import</span> YoutubeDL
<span style="color: #ff0000">from</span> discord_slash <span style="color: #ff0000">import</span> SlashCommand
<span style="color: #ff0000">from</span> discord_slash.model <span style="color: #ff0000">import</span> ButtonStyle
<span style="color: #ff0000">from</span> discord_slash.utils.manage_components <span style="color: #ff0000">import</span> create_button, create_actionrow
<span style="color: #ff0000">from</span> discord_slash.utils.manage_components <span style="color: #ff0000">import</span> ComponentContext, wait_for_component

bot = commands.Bot(command_prefix=<span style="color: #87ceeb">&#39;.&#39;</span>, help_command=None)

slash = SlashCommand(bot,
                     sync_commands=True,
                     sync_on_cog_reload=True,
                     application_id=916685474364534805)

beats_activity = [discord.ActivityType.listening, <span style="color: #87ceeb">&quot;Beats&quot;</span>]

extensions = [<span style="color: #87ceeb">&quot;music&quot;</span>, <span style="color: #87ceeb">&quot;general&quot;</span>]
bot.load_extension(<span style="color: #87ceeb">&quot;music&quot;</span>)
bot.load_extension(<span style="color: #87ceeb">&quot;general&quot;</span>)
bot.load_extension(<span style="color: #87ceeb">&quot;slashcog&quot;</span>)
IST = pytz.timezone(<span style="color: #87ceeb">&#39;Asia/Kolkata&#39;</span>)


@bot.event
<span style="color: #00ff00">#on ready</span>
async <span style="color: #ff0000">def</span> <span style="color: #ffff00">on_ready</span>():
    <span style="color: #ff0000">print</span>(<span style="color: #87ceeb">&quot;logged in as {0.user}&quot;</span>.format(bot))
    await bot.change_presence(activity=discord.Activity(
        type=beats_activity[0], name=beats_activity[1]),
                              status=discord.Status.dnd)


@bot.event
async <span style="color: #ff0000">def</span> <span style="color: #ffff00">on_message</span>(msg):
    <span style="color: #ff0000">if</span> (msg.author.bot):
        <span style="color: #ff0000">return</span>
    allstr = tuple(KEYWORD)
    authid = str(msg.author.id)
    authname = msg.author
    <span style="color: #ff0000">with</span> open(<span style="color: #87ceeb">&quot;json.json&quot;</span>, <span style="color: #87ceeb">&quot;r&quot;</span>) <span style="color: #ff0000">as</span> jsonfile:
        jsonfile = json.load(jsonfile)
    <span style="color: #ff0000">if</span> msg.content.startswith(allstr):

        <span style="color: #ff0000">with</span> open(<span style="color: #87ceeb">&quot;json.json&quot;</span>, <span style="color: #87ceeb">&quot;w&quot;</span>) <span style="color: #ff0000">as</span> f:
            <span style="color: #ff0000">if</span> authid in jsonfile:
                time_ = datetime.datetime.now(IST)
                <span style="color: #ff0000">try</span>:
                    content = {
                        <span style="color: #87ceeb">&quot;message&quot;</span>: msg.content,
                        <span style="color: #87ceeb">&quot;time&quot;</span>: time_.strftime(<span style="color: #87ceeb">&quot;%d/%m/%Y %I:%M %p&quot;</span>),
                        <span style="color: #87ceeb">&quot;guild&quot;</span>: msg.author.guild.name
                    }
                <span style="color: #ff0000">except</span> AttributeError:
                    content = {
                        <span style="color: #87ceeb">&quot;message&quot;</span>: msg.content,
                        <span style="color: #87ceeb">&quot;time&quot;</span>: time_.strftime(<span style="color: #87ceeb">&quot;%d/%m/%Y %I:%M %p&quot;</span>),
                        <span style="color: #87ceeb">&quot;guild&quot;</span>: <span style="color: #87ceeb">&quot;DM&quot;</span>
                    }

                <span style="color: #ff0000">else</span>:
                    content = {
                        <span style="color: #87ceeb">&quot;message&quot;</span>: msg.content,
                        <span style="color: #87ceeb">&quot;time&quot;</span>: time_.strftime(<span style="color: #87ceeb">&quot;%d/%m/%Y %I:%M %p&quot;</span>),
                        <span style="color: #87ceeb">&quot;guild&quot;</span>: msg.author.guild.name
                    }
                jsonfile[authid][<span style="color: #87ceeb">&quot;messages&quot;</span>].append(content)
                json.dump(jsonfile, f, indent=7)
            <span style="color: #ff0000">else</span>:
                time_ = datetime.datetime.now(IST)
                jsonfile[authid] = {
                    <span style="color: #87ceeb">&quot;id&quot;</span>: int(authid),
                    <span style="color: #87ceeb">&quot;name&quot;</span>: f<span style="color: #87ceeb">&quot;{authname}&quot;</span>,
                    <span style="color: #87ceeb">&quot;messages&quot;</span>: []
                }
                <span style="color: #ff0000">try</span>:
                    content = {
                        <span style="color: #87ceeb">&quot;message&quot;</span>: msg.content,
                        <span style="color: #87ceeb">&quot;time&quot;</span>: time_.strftime(<span style="color: #87ceeb">&quot;%d/%m/%Y %I:%M %p&quot;</span>),
                        <span style="color: #87ceeb">&quot;guild&quot;</span>: msg.author.guild.name
                    }
                <span style="color: #ff0000">except</span> AttributeError:
                    content = {
                        <span style="color: #87ceeb">&quot;message&quot;</span>: msg.content,
                        <span style="color: #87ceeb">&quot;time&quot;</span>: time_.strftime(<span style="color: #87ceeb">&quot;%d/%m/%Y %I:%M %p&quot;</span>),
                        <span style="color: #87ceeb">&quot;guild&quot;</span>: <span style="color: #87ceeb">&quot;DM&quot;</span>
                    }

                <span style="color: #ff0000">else</span>:
                    content = {
                        <span style="color: #87ceeb">&quot;message&quot;</span>: msg.content,
                        <span style="color: #87ceeb">&quot;time&quot;</span>: time_.strftime(<span style="color: #87ceeb">&quot;%d/%m/%Y %I:%M %p&quot;</span>),
                        <span style="color: #87ceeb">&quot;guild&quot;</span>: msg.author.guild.name
                    }
                jsonfile[authid][<span style="color: #87ceeb">&quot;messages&quot;</span>].append(content)
                json.dump(jsonfile, f, indent=7)
    await bot.process_commands(msg)


@bot.command()
async <span style="color: #ff0000">def</span> <span style="color: #ffff00">gs</span>(ctx, query):
    await ctx.author.send(f<span style="color: #87ceeb">&quot;Here are the links related to your question!&quot;</span>)
    <span style="color: #ff0000">for</span> j in search(query, safe=<span style="color: #87ceeb">&#39;on&#39;</span>, start=1, stop=1):
        await ctx.author.send(f<span style="color: #87ceeb">&quot;\n:point_right: {j}&quot;</span>)
        await ctx.author.send(
            <span style="color: #87ceeb">&quot;Have any more questions:question:\nFeel free to ask again :smiley: !&quot;</span>
        )


NEXTBUTTON = [
    create_button(ButtonStyle.green, label=<span style="color: #87ceeb">&quot;Next&quot;</span>, custom_id=<span style="color: #87ceeb">&quot;NextMeme&quot;</span>)
]


@bot.command(name=<span style="color: #87ceeb">&quot;meme&quot;</span>)
async <span style="color: #ff0000">def</span> <span style="color: #ffff00">meme_</span>(ctx):
    em = func.meme()
    await ctx.send(embed=em, components=[create_actionrow(*NEXTBUTTON)])

    <span style="color: #ff0000">while</span> 1:
        <span style="color: #ff0000">try</span>:
            button_ctx: ComponentContext = await wait_for_component(
                bot, components=NEXTBUTTON, timeout=10)
            await button_ctx.edit_origin(embed=func.meme())
        <span style="color: #ff0000">except</span> asyncio.exceptions.TimeoutError:
            <span style="color: #ff0000">break</span>


TOKEN = os.getenv(<span style="color: #87ceeb">&quot;TOKEN&quot;</span>)
keep_alive.keep_alive()
bot.run(TOKEN)  <span style="color: #00ff00"># client login</span>
</pre></td></tr></table></div>
''',
'''
<!-- HTML generated using hilite.me --><div style="background: #000000; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #cd00cd">import</span> <span style="color: #cccccc">os</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">sys</span>

<span style="color: #cccccc">sys</span><span style="color: #3399cc">.</span><span style="color: #cccccc">path</span><span style="color: #3399cc">.</span><span style="color: #cccccc">insert(</span><span style="color: #cd00cd">1</span><span style="color: #cccccc">,</span> <span style="color: #cd0000">&#39;./modules&#39;</span><span style="color: #cccccc">)</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">json</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">pytz</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">asyncio</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">discord</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">datetime</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">keep_alive</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">youtube_dl</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">discord_slash</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">os</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">getenv</span>
<span style="color: #cd00cd">import</span> <span style="color: #cccccc">impfunctions</span> <span style="color: #cd00cd">as</span> <span style="color: #cccccc">func</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">keywords</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">KEYWORD</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">googlesearch</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">search</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">discord.ext</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">commands</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">youtube_dl</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">YoutubeDL</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">discord_slash</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">SlashCommand</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">discord_slash.model</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">ButtonStyle</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">discord_slash.utils.manage_components</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">create_button,</span> <span style="color: #cccccc">create_actionrow</span>
<span style="color: #cd00cd">from</span> <span style="color: #cccccc">discord_slash.utils.manage_components</span> <span style="color: #cd00cd">import</span> <span style="color: #cccccc">ComponentContext,</span> <span style="color: #cccccc">wait_for_component</span>

<span style="color: #cccccc">bot</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">commands</span><span style="color: #3399cc">.</span><span style="color: #cccccc">Bot(command_prefix</span><span style="color: #3399cc">=</span><span style="color: #cd0000">&#39;.&#39;</span><span style="color: #cccccc">,</span> <span style="color: #cccccc">help_command</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">None</span><span style="color: #cccccc">)</span>

<span style="color: #cccccc">slash</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">SlashCommand(bot,</span>
                     <span style="color: #cccccc">sync_commands</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">True</span><span style="color: #cccccc">,</span>
                     <span style="color: #cccccc">sync_on_cog_reload</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">True</span><span style="color: #cccccc">,</span>
                     <span style="color: #cccccc">application_id</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">916685474364534805</span><span style="color: #cccccc">)</span>

<span style="color: #cccccc">beats_activity</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">[discord</span><span style="color: #3399cc">.</span><span style="color: #cccccc">ActivityType</span><span style="color: #3399cc">.</span><span style="color: #cccccc">listening,</span> <span style="color: #cd0000">&quot;Beats&quot;</span><span style="color: #cccccc">]</span>

<span style="color: #cccccc">extensions</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">[</span><span style="color: #cd0000">&quot;music&quot;</span><span style="color: #cccccc">,</span> <span style="color: #cd0000">&quot;general&quot;</span><span style="color: #cccccc">]</span>
<span style="color: #cccccc">bot</span><span style="color: #3399cc">.</span><span style="color: #cccccc">load_extension(</span><span style="color: #cd0000">&quot;music&quot;</span><span style="color: #cccccc">)</span>
<span style="color: #cccccc">bot</span><span style="color: #3399cc">.</span><span style="color: #cccccc">load_extension(</span><span style="color: #cd0000">&quot;general&quot;</span><span style="color: #cccccc">)</span>
<span style="color: #cccccc">bot</span><span style="color: #3399cc">.</span><span style="color: #cccccc">load_extension(</span><span style="color: #cd0000">&quot;slashcog&quot;</span><span style="color: #cccccc">)</span>
<span style="color: #cccccc">IST</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">pytz</span><span style="color: #3399cc">.</span><span style="color: #cccccc">timezone(</span><span style="color: #cd0000">&#39;Asia/Kolkata&#39;</span><span style="color: #cccccc">)</span>


<span style="color: #cccccc">@bot.event</span>
<span style="color: #000080">#on ready</span>
<span style="color: #cccccc">async</span> <span style="color: #cdcd00">def</span> <span style="color: #cccccc">on_ready():</span>
    <span style="color: #cdcd00">print</span><span style="color: #cccccc">(</span><span style="color: #cd0000">&quot;logged in as {0.user}&quot;</span><span style="color: #3399cc">.</span><span style="color: #cccccc">format(bot))</span>
    <span style="color: #cccccc">await</span> <span style="color: #cccccc">bot</span><span style="color: #3399cc">.</span><span style="color: #cccccc">change_presence(activity</span><span style="color: #3399cc">=</span><span style="color: #cccccc">discord</span><span style="color: #3399cc">.</span><span style="color: #cccccc">Activity(</span>
        <span style="color: #cd00cd">type</span><span style="color: #3399cc">=</span><span style="color: #cccccc">beats_activity[</span><span style="color: #cd00cd">0</span><span style="color: #cccccc">],</span> <span style="color: #cccccc">name</span><span style="color: #3399cc">=</span><span style="color: #cccccc">beats_activity[</span><span style="color: #cd00cd">1</span><span style="color: #cccccc">]),</span>
                              <span style="color: #cccccc">status</span><span style="color: #3399cc">=</span><span style="color: #cccccc">discord</span><span style="color: #3399cc">.</span><span style="color: #cccccc">Status</span><span style="color: #3399cc">.</span><span style="color: #cccccc">dnd)</span>


<span style="color: #cccccc">@bot.event</span>
<span style="color: #cccccc">async</span> <span style="color: #cdcd00">def</span> <span style="color: #cccccc">on_message(msg):</span>
    <span style="color: #cdcd00">if</span> <span style="color: #cccccc">(msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">bot):</span>
        <span style="color: #cdcd00">return</span>
    <span style="color: #cccccc">allstr</span> <span style="color: #3399cc">=</span> <span style="color: #cd00cd">tuple</span><span style="color: #cccccc">(KEYWORD)</span>
    <span style="color: #cccccc">authid</span> <span style="color: #3399cc">=</span> <span style="color: #cd00cd">str</span><span style="color: #cccccc">(msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">id)</span>
    <span style="color: #cccccc">authname</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span>
    <span style="color: #cdcd00">with</span> <span style="color: #cd00cd">open</span><span style="color: #cccccc">(</span><span style="color: #cd0000">&quot;json.json&quot;</span><span style="color: #cccccc">,</span> <span style="color: #cd0000">&quot;r&quot;</span><span style="color: #cccccc">)</span> <span style="color: #cdcd00">as</span> <span style="color: #cccccc">jsonfile:</span>
        <span style="color: #cccccc">jsonfile</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">json</span><span style="color: #3399cc">.</span><span style="color: #cccccc">load(jsonfile)</span>
    <span style="color: #cdcd00">if</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content</span><span style="color: #3399cc">.</span><span style="color: #cccccc">startswith(allstr):</span>

        <span style="color: #cdcd00">with</span> <span style="color: #cd00cd">open</span><span style="color: #cccccc">(</span><span style="color: #cd0000">&quot;json.json&quot;</span><span style="color: #cccccc">,</span> <span style="color: #cd0000">&quot;w&quot;</span><span style="color: #cccccc">)</span> <span style="color: #cdcd00">as</span> <span style="color: #cccccc">f:</span>
            <span style="color: #cdcd00">if</span> <span style="color: #cccccc">authid</span> <span style="color: #cdcd00">in</span> <span style="color: #cccccc">jsonfile:</span>
                <span style="color: #cccccc">time_</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">datetime</span><span style="color: #3399cc">.</span><span style="color: #cccccc">datetime</span><span style="color: #3399cc">.</span><span style="color: #cccccc">now(IST)</span>
                <span style="color: #cdcd00">try</span><span style="color: #cccccc">:</span>
                    <span style="color: #cccccc">content</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                        <span style="color: #cd0000">&quot;message&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content,</span>
                        <span style="color: #cd0000">&quot;time&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">time_</span><span style="color: #3399cc">.</span><span style="color: #cccccc">strftime(</span><span style="color: #cd0000">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #cccccc">),</span>
                        <span style="color: #cd0000">&quot;guild&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">guild</span><span style="color: #3399cc">.</span><span style="color: #cccccc">name</span>
                    <span style="color: #cccccc">}</span>
                <span style="color: #cdcd00">except</span> <span style="color: #666699; font-weight: bold">AttributeError</span><span style="color: #cccccc">:</span>
                    <span style="color: #cccccc">content</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                        <span style="color: #cd0000">&quot;message&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content,</span>
                        <span style="color: #cd0000">&quot;time&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">time_</span><span style="color: #3399cc">.</span><span style="color: #cccccc">strftime(</span><span style="color: #cd0000">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #cccccc">),</span>
                        <span style="color: #cd0000">&quot;guild&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cd0000">&quot;DM&quot;</span>
                    <span style="color: #cccccc">}</span>

                <span style="color: #cdcd00">else</span><span style="color: #cccccc">:</span>
                    <span style="color: #cccccc">content</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                        <span style="color: #cd0000">&quot;message&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content,</span>
                        <span style="color: #cd0000">&quot;time&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">time_</span><span style="color: #3399cc">.</span><span style="color: #cccccc">strftime(</span><span style="color: #cd0000">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #cccccc">),</span>
                        <span style="color: #cd0000">&quot;guild&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">guild</span><span style="color: #3399cc">.</span><span style="color: #cccccc">name</span>
                    <span style="color: #cccccc">}</span>
                <span style="color: #cccccc">jsonfile[authid][</span><span style="color: #cd0000">&quot;messages&quot;</span><span style="color: #cccccc">]</span><span style="color: #3399cc">.</span><span style="color: #cccccc">append(content)</span>
                <span style="color: #cccccc">json</span><span style="color: #3399cc">.</span><span style="color: #cccccc">dump(jsonfile,</span> <span style="color: #cccccc">f,</span> <span style="color: #cccccc">indent</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">7</span><span style="color: #cccccc">)</span>
            <span style="color: #cdcd00">else</span><span style="color: #cccccc">:</span>
                <span style="color: #cccccc">time_</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">datetime</span><span style="color: #3399cc">.</span><span style="color: #cccccc">datetime</span><span style="color: #3399cc">.</span><span style="color: #cccccc">now(IST)</span>
                <span style="color: #cccccc">jsonfile[authid]</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                    <span style="color: #cd0000">&quot;id&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cd00cd">int</span><span style="color: #cccccc">(authid),</span>
                    <span style="color: #cd0000">&quot;name&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">f</span><span style="color: #cd0000">&quot;{authname}&quot;</span><span style="color: #cccccc">,</span>
                    <span style="color: #cd0000">&quot;messages&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">[]</span>
                <span style="color: #cccccc">}</span>
                <span style="color: #cdcd00">try</span><span style="color: #cccccc">:</span>
                    <span style="color: #cccccc">content</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                        <span style="color: #cd0000">&quot;message&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content,</span>
                        <span style="color: #cd0000">&quot;time&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">time_</span><span style="color: #3399cc">.</span><span style="color: #cccccc">strftime(</span><span style="color: #cd0000">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #cccccc">),</span>
                        <span style="color: #cd0000">&quot;guild&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">guild</span><span style="color: #3399cc">.</span><span style="color: #cccccc">name</span>
                    <span style="color: #cccccc">}</span>
                <span style="color: #cdcd00">except</span> <span style="color: #666699; font-weight: bold">AttributeError</span><span style="color: #cccccc">:</span>
                    <span style="color: #cccccc">content</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                        <span style="color: #cd0000">&quot;message&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content,</span>
                        <span style="color: #cd0000">&quot;time&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">time_</span><span style="color: #3399cc">.</span><span style="color: #cccccc">strftime(</span><span style="color: #cd0000">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #cccccc">),</span>
                        <span style="color: #cd0000">&quot;guild&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cd0000">&quot;DM&quot;</span>
                    <span style="color: #cccccc">}</span>

                <span style="color: #cdcd00">else</span><span style="color: #cccccc">:</span>
                    <span style="color: #cccccc">content</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">{</span>
                        <span style="color: #cd0000">&quot;message&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">content,</span>
                        <span style="color: #cd0000">&quot;time&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">time_</span><span style="color: #3399cc">.</span><span style="color: #cccccc">strftime(</span><span style="color: #cd0000">&quot;%d/%m/%Y %I:%M %p&quot;</span><span style="color: #cccccc">),</span>
                        <span style="color: #cd0000">&quot;guild&quot;</span><span style="color: #cccccc">:</span> <span style="color: #cccccc">msg</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">guild</span><span style="color: #3399cc">.</span><span style="color: #cccccc">name</span>
                    <span style="color: #cccccc">}</span>
                <span style="color: #cccccc">jsonfile[authid][</span><span style="color: #cd0000">&quot;messages&quot;</span><span style="color: #cccccc">]</span><span style="color: #3399cc">.</span><span style="color: #cccccc">append(content)</span>
                <span style="color: #cccccc">json</span><span style="color: #3399cc">.</span><span style="color: #cccccc">dump(jsonfile,</span> <span style="color: #cccccc">f,</span> <span style="color: #cccccc">indent</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">7</span><span style="color: #cccccc">)</span>
    <span style="color: #cccccc">await</span> <span style="color: #cccccc">bot</span><span style="color: #3399cc">.</span><span style="color: #cccccc">process_commands(msg)</span>


<span style="color: #cccccc">@bot.command()</span>
<span style="color: #cccccc">async</span> <span style="color: #cdcd00">def</span> <span style="color: #cccccc">gs(ctx,</span> <span style="color: #cccccc">query):</span>
    <span style="color: #cccccc">await</span> <span style="color: #cccccc">ctx</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">send(f</span><span style="color: #cd0000">&quot;Here are the links related to your question!&quot;</span><span style="color: #cccccc">)</span>
    <span style="color: #cdcd00">for</span> <span style="color: #cccccc">j</span> <span style="color: #cdcd00">in</span> <span style="color: #cccccc">search(query,</span> <span style="color: #cccccc">safe</span><span style="color: #3399cc">=</span><span style="color: #cd0000">&#39;on&#39;</span><span style="color: #cccccc">,</span> <span style="color: #cccccc">start</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">1</span><span style="color: #cccccc">,</span> <span style="color: #cccccc">stop</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">1</span><span style="color: #cccccc">):</span>
        <span style="color: #cccccc">await</span> <span style="color: #cccccc">ctx</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">send(f</span><span style="color: #cd0000">&quot;\n:point_right: {j}&quot;</span><span style="color: #cccccc">)</span>
        <span style="color: #cccccc">await</span> <span style="color: #cccccc">ctx</span><span style="color: #3399cc">.</span><span style="color: #cccccc">author</span><span style="color: #3399cc">.</span><span style="color: #cccccc">send(</span>
            <span style="color: #cd0000">&quot;Have any more questions:question:\nFeel free to ask again :smiley: !&quot;</span>
        <span style="color: #cccccc">)</span>


<span style="color: #cccccc">NEXTBUTTON</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">[</span>
    <span style="color: #cccccc">create_button(ButtonStyle</span><span style="color: #3399cc">.</span><span style="color: #cccccc">green,</span> <span style="color: #cccccc">label</span><span style="color: #3399cc">=</span><span style="color: #cd0000">&quot;Next&quot;</span><span style="color: #cccccc">,</span> <span style="color: #cccccc">custom_id</span><span style="color: #3399cc">=</span><span style="color: #cd0000">&quot;NextMeme&quot;</span><span style="color: #cccccc">)</span>
<span style="color: #cccccc">]</span>


<span style="color: #cccccc">@bot.command(name</span><span style="color: #3399cc">=</span><span style="color: #cd0000">&quot;meme&quot;</span><span style="color: #cccccc">)</span>
<span style="color: #cccccc">async</span> <span style="color: #cdcd00">def</span> <span style="color: #cccccc">meme_(ctx):</span>
    <span style="color: #cccccc">em</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">func</span><span style="color: #3399cc">.</span><span style="color: #cccccc">meme()</span>
    <span style="color: #cccccc">await</span> <span style="color: #cccccc">ctx</span><span style="color: #3399cc">.</span><span style="color: #cccccc">send(embed</span><span style="color: #3399cc">=</span><span style="color: #cccccc">em,</span> <span style="color: #cccccc">components</span><span style="color: #3399cc">=</span><span style="color: #cccccc">[create_actionrow(</span><span style="color: #3399cc">*</span><span style="color: #cccccc">NEXTBUTTON)])</span>

    <span style="color: #cdcd00">while</span> <span style="color: #cd00cd">1</span><span style="color: #cccccc">:</span>
        <span style="color: #cdcd00">try</span><span style="color: #cccccc">:</span>
            <span style="color: #cccccc">button_ctx:</span> <span style="color: #cccccc">ComponentContext</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">await</span> <span style="color: #cccccc">wait_for_component(</span>
                <span style="color: #cccccc">bot,</span> <span style="color: #cccccc">components</span><span style="color: #3399cc">=</span><span style="color: #cccccc">NEXTBUTTON,</span> <span style="color: #cccccc">timeout</span><span style="color: #3399cc">=</span><span style="color: #cd00cd">10</span><span style="color: #cccccc">)</span>
            <span style="color: #cccccc">await</span> <span style="color: #cccccc">button_ctx</span><span style="color: #3399cc">.</span><span style="color: #cccccc">edit_origin(embed</span><span style="color: #3399cc">=</span><span style="color: #cccccc">func</span><span style="color: #3399cc">.</span><span style="color: #cccccc">meme())</span>
        <span style="color: #cdcd00">except</span> <span style="color: #cccccc">asyncio</span><span style="color: #3399cc">.</span><span style="color: #cccccc">exceptions</span><span style="color: #3399cc">.</span><span style="color: #cccccc">TimeoutError:</span>
            <span style="color: #cdcd00">break</span>


<span style="color: #cccccc">TOKEN</span> <span style="color: #3399cc">=</span> <span style="color: #cccccc">os</span><span style="color: #3399cc">.</span><span style="color: #cccccc">getenv(</span><span style="color: #cd0000">&quot;TOKEN&quot;</span><span style="color: #cccccc">)</span>
<span style="color: #cccccc">keep_alive</span><span style="color: #3399cc">.</span><span style="color: #cccccc">keep_alive()</span>
<span style="color: #cccccc">bot</span><span style="color: #3399cc">.</span><span style="color: #cccccc">run(TOKEN)</span>  <span style="color: #000080"># client login</span>
</pre></td></tr></table></div>
'''

]