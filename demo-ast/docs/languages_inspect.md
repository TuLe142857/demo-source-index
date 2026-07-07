
# C

- Language: c
- ABI version: 15
- File name extensions: ['.c', '.h']
- File name patterns: []
- Node kinds count: 363
    - Anonymous node count: 203
    - Visible node count: 304
    - Supertype node count: 311
- Field count: 39

## Node kinds

|   id | name                                                  | is_named   | is_supertype   | subtype_ids                                                                                                                      | is_visible   |
|------|-------------------------------------------------------|------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|--------------|
|    0 | end                                                   | False      | False          | ()                                                                                                                               | False        |
|    1 | identifier                                            | True       | True           | ()                                                                                                                               | True         |
|    2 | #include                                              | False      | True           | ()                                                                                                                               | True         |
|    3 | preproc\_include\_token2                              | False      | False          | ()                                                                                                                               | False        |
|    4 | #define                                               | False      | True           | ()                                                                                                                               | True         |
|    5 | (                                                     | False      | True           | ()                                                                                                                               | True         |
|    6 | ...                                                   | False      | True           | ()                                                                                                                               | True         |
|    7 | ,                                                     | False      | True           | ()                                                                                                                               | True         |
|    8 | )                                                     | False      | True           | ()                                                                                                                               | True         |
|    9 | #if                                                   | False      | True           | ()                                                                                                                               | True         |
|   10 |                                                       | False      | True           | ()                                                                                                                               | True         |
|   11 | #endif                                                | False      | True           | ()                                                                                                                               | True         |
|   12 | #ifdef                                                | False      | True           | ()                                                                                                                               | True         |
|   13 | #ifndef                                               | False      | True           | ()                                                                                                                               | True         |
|   14 | #else                                                 | False      | True           | ()                                                                                                                               | True         |
|   15 | #elif                                                 | False      | True           | ()                                                                                                                               | True         |
|   16 | #elifdef                                              | False      | True           | ()                                                                                                                               | True         |
|   17 | #elifndef                                             | False      | True           | ()                                                                                                                               | True         |
|   18 | preproc\_arg                                          | True       | True           | ()                                                                                                                               | True         |
|   19 | preproc\_directive                                    | True       | True           | ()                                                                                                                               | True         |
|   20 | (                                                     | False      | True           | ()                                                                                                                               | True         |
|   21 | defined                                               | False      | True           | ()                                                                                                                               | True         |
|   22 | !                                                     | False      | True           | ()                                                                                                                               | True         |
|   23 | ~                                                     | False      | True           | ()                                                                                                                               | True         |
|   24 | -                                                     | False      | True           | ()                                                                                                                               | True         |
|   25 | +                                                     | False      | True           | ()                                                                                                                               | True         |
|   26 | \*                                                    | False      | True           | ()                                                                                                                               | True         |
|   27 | /                                                     | False      | True           | ()                                                                                                                               | True         |
|   28 | %                                                     | False      | True           | ()                                                                                                                               | True         |
|   29 | &#124;&#124;                                          | False      | True           | ()                                                                                                                               | True         |
|   30 | &amp;&amp;                                            | False      | True           | ()                                                                                                                               | True         |
|   31 | &#124;                                                | False      | True           | ()                                                                                                                               | True         |
|   32 | ^                                                     | False      | True           | ()                                                                                                                               | True         |
|   33 | &amp;                                                 | False      | True           | ()                                                                                                                               | True         |
|   34 | ==                                                    | False      | True           | ()                                                                                                                               | True         |
|   35 | !=                                                    | False      | True           | ()                                                                                                                               | True         |
|   36 | &gt;                                                  | False      | True           | ()                                                                                                                               | True         |
|   37 | &gt;=                                                 | False      | True           | ()                                                                                                                               | True         |
|   38 | &lt;=                                                 | False      | True           | ()                                                                                                                               | True         |
|   39 | &lt;                                                  | False      | True           | ()                                                                                                                               | True         |
|   40 | &lt;&lt;                                              | False      | True           | ()                                                                                                                               | True         |
|   41 | &gt;&gt;                                              | False      | True           | ()                                                                                                                               | True         |
|   42 | ;                                                     | False      | True           | ()                                                                                                                               | True         |
|   43 | \_\_extension\_\_                                     | False      | True           | ()                                                                                                                               | True         |
|   44 | typedef                                               | False      | True           | ()                                                                                                                               | True         |
|   45 | extern                                                | False      | True           | ()                                                                                                                               | True         |
|   46 | \_\_attribute\_\_                                     | False      | True           | ()                                                                                                                               | True         |
|   47 | \_\_attribute                                         | False      | True           | ()                                                                                                                               | True         |
|   48 | ::                                                    | False      | True           | ()                                                                                                                               | True         |
|   49 | [[                                                    | False      | True           | ()                                                                                                                               | True         |
|   50 | ]]                                                    | False      | True           | ()                                                                                                                               | True         |
|   51 | \_\_declspec                                          | False      | True           | ()                                                                                                                               | True         |
|   52 | \_\_based                                             | False      | True           | ()                                                                                                                               | True         |
|   53 | \_\_cdecl                                             | False      | True           | ()                                                                                                                               | True         |
|   54 | \_\_clrcall                                           | False      | True           | ()                                                                                                                               | True         |
|   55 | \_\_stdcall                                           | False      | True           | ()                                                                                                                               | True         |
|   56 | \_\_fastcall                                          | False      | True           | ()                                                                                                                               | True         |
|   57 | \_\_thiscall                                          | False      | True           | ()                                                                                                                               | True         |
|   58 | \_\_vectorcall                                        | False      | True           | ()                                                                                                                               | True         |
|   59 | ms\_restrict\_modifier                                | True       | True           | ()                                                                                                                               | True         |
|   60 | ms\_unsigned\_ptr\_modifier                           | True       | True           | ()                                                                                                                               | True         |
|   61 | ms\_signed\_ptr\_modifier                             | True       | True           | ()                                                                                                                               | True         |
|   62 | \_unaligned                                           | False      | True           | ()                                                                                                                               | True         |
|   63 | \_\_unaligned                                         | False      | True           | ()                                                                                                                               | True         |
|   64 | {                                                     | False      | True           | ()                                                                                                                               | True         |
|   65 | }                                                     | False      | True           | ()                                                                                                                               | True         |
|   66 | signed                                                | False      | True           | ()                                                                                                                               | True         |
|   67 | unsigned                                              | False      | True           | ()                                                                                                                               | True         |
|   68 | long                                                  | False      | True           | ()                                                                                                                               | True         |
|   69 | short                                                 | False      | True           | ()                                                                                                                               | True         |
|   70 | [                                                     | False      | True           | ()                                                                                                                               | True         |
|   71 | static                                                | False      | True           | ()                                                                                                                               | True         |
|   72 | ]                                                     | False      | True           | ()                                                                                                                               | True         |
|   73 | =                                                     | False      | True           | ()                                                                                                                               | True         |
|   74 | auto                                                  | False      | True           | ()                                                                                                                               | True         |
|   75 | register                                              | False      | True           | ()                                                                                                                               | True         |
|   76 | inline                                                | False      | True           | ()                                                                                                                               | True         |
|   77 | \_\_inline                                            | False      | True           | ()                                                                                                                               | True         |
|   78 | \_\_inline\_\_                                        | False      | True           | ()                                                                                                                               | True         |
|   79 | \_\_forceinline                                       | False      | True           | ()                                                                                                                               | True         |
|   80 | thread\_local                                         | False      | True           | ()                                                                                                                               | True         |
|   81 | \_\_thread                                            | False      | True           | ()                                                                                                                               | True         |
|   82 | const                                                 | False      | True           | ()                                                                                                                               | True         |
|   83 | constexpr                                             | False      | True           | ()                                                                                                                               | True         |
|   84 | volatile                                              | False      | True           | ()                                                                                                                               | True         |
|   85 | restrict                                              | False      | True           | ()                                                                                                                               | True         |
|   86 | \_\_restrict\_\_                                      | False      | True           | ()                                                                                                                               | True         |
|   87 | \_Atomic                                              | False      | True           | ()                                                                                                                               | True         |
|   88 | \_Noreturn                                            | False      | True           | ()                                                                                                                               | True         |
|   89 | noreturn                                              | False      | True           | ()                                                                                                                               | True         |
|   90 | \_Nonnull                                             | False      | True           | ()                                                                                                                               | True         |
|   91 | alignas                                               | False      | True           | ()                                                                                                                               | True         |
|   92 | \_Alignas                                             | False      | True           | ()                                                                                                                               | True         |
|   93 | primitive\_type                                       | True       | True           | ()                                                                                                                               | True         |
|   94 | enum                                                  | False      | True           | ()                                                                                                                               | True         |
|   95 | :                                                     | False      | True           | ()                                                                                                                               | True         |
|   96 | struct                                                | False      | True           | ()                                                                                                                               | True         |
|   97 | union                                                 | False      | True           | ()                                                                                                                               | True         |
|   98 | if                                                    | False      | True           | ()                                                                                                                               | True         |
|   99 | else                                                  | False      | True           | ()                                                                                                                               | True         |
|  100 | switch                                                | False      | True           | ()                                                                                                                               | True         |
|  101 | case                                                  | False      | True           | ()                                                                                                                               | True         |
|  102 | default                                               | False      | True           | ()                                                                                                                               | True         |
|  103 | while                                                 | False      | True           | ()                                                                                                                               | True         |
|  104 | do                                                    | False      | True           | ()                                                                                                                               | True         |
|  105 | for                                                   | False      | True           | ()                                                                                                                               | True         |
|  106 | return                                                | False      | True           | ()                                                                                                                               | True         |
|  107 | break                                                 | False      | True           | ()                                                                                                                               | True         |
|  108 | continue                                              | False      | True           | ()                                                                                                                               | True         |
|  109 | goto                                                  | False      | True           | ()                                                                                                                               | True         |
|  110 | \_\_try                                               | False      | True           | ()                                                                                                                               | True         |
|  111 | \_\_except                                            | False      | True           | ()                                                                                                                               | True         |
|  112 | \_\_finally                                           | False      | True           | ()                                                                                                                               | True         |
|  113 | \_\_leave                                             | False      | True           | ()                                                                                                                               | True         |
|  114 | ?                                                     | False      | True           | ()                                                                                                                               | True         |
|  115 | \*=                                                   | False      | True           | ()                                                                                                                               | True         |
|  116 | /=                                                    | False      | True           | ()                                                                                                                               | True         |
|  117 | %=                                                    | False      | True           | ()                                                                                                                               | True         |
|  118 | +=                                                    | False      | True           | ()                                                                                                                               | True         |
|  119 | -=                                                    | False      | True           | ()                                                                                                                               | True         |
|  120 | &lt;&lt;=                                             | False      | True           | ()                                                                                                                               | True         |
|  121 | &gt;&gt;=                                             | False      | True           | ()                                                                                                                               | True         |
|  122 | &amp;=                                                | False      | True           | ()                                                                                                                               | True         |
|  123 | ^=                                                    | False      | True           | ()                                                                                                                               | True         |
|  124 | &#124;=                                               | False      | True           | ()                                                                                                                               | True         |
|  125 | --                                                    | False      | True           | ()                                                                                                                               | True         |
|  126 | ++                                                    | False      | True           | ()                                                                                                                               | True         |
|  127 | sizeof                                                | False      | True           | ()                                                                                                                               | True         |
|  128 | \_\_alignof\_\_                                       | False      | True           | ()                                                                                                                               | True         |
|  129 | \_\_alignof                                           | False      | True           | ()                                                                                                                               | True         |
|  130 | \_alignof                                             | False      | True           | ()                                                                                                                               | True         |
|  131 | alignof                                               | False      | True           | ()                                                                                                                               | True         |
|  132 | \_Alignof                                             | False      | True           | ()                                                                                                                               | True         |
|  133 | offsetof                                              | False      | True           | ()                                                                                                                               | True         |
|  134 | \_Generic                                             | False      | True           | ()                                                                                                                               | True         |
|  135 | asm                                                   | False      | True           | ()                                                                                                                               | True         |
|  136 | \_\_asm\_\_                                           | False      | True           | ()                                                                                                                               | True         |
|  137 | \_\_asm                                               | False      | True           | ()                                                                                                                               | True         |
|  138 | \_\_volatile\_\_                                      | False      | True           | ()                                                                                                                               | True         |
|  139 | .                                                     | False      | True           | ()                                                                                                                               | True         |
|  140 | -&gt;                                                 | False      | True           | ()                                                                                                                               | True         |
|  141 | number\_literal                                       | True       | True           | ()                                                                                                                               | True         |
|  142 | L'                                                    | False      | True           | ()                                                                                                                               | True         |
|  143 | u'                                                    | False      | True           | ()                                                                                                                               | True         |
|  144 | U'                                                    | False      | True           | ()                                                                                                                               | True         |
|  145 | u8'                                                   | False      | True           | ()                                                                                                                               | True         |
|  146 | '                                                     | False      | True           | ()                                                                                                                               | True         |
|  147 | character                                             | True       | True           | ()                                                                                                                               | True         |
|  148 | L"                                                    | False      | True           | ()                                                                                                                               | True         |
|  149 | u"                                                    | False      | True           | ()                                                                                                                               | True         |
|  150 | U"                                                    | False      | True           | ()                                                                                                                               | True         |
|  151 | u8"                                                   | False      | True           | ()                                                                                                                               | True         |
|  152 | "                                                     | False      | True           | ()                                                                                                                               | True         |
|  153 | string\_content                                       | True       | True           | ()                                                                                                                               | True         |
|  154 | escape\_sequence                                      | True       | True           | ()                                                                                                                               | True         |
|  155 | system\_lib\_string                                   | True       | True           | ()                                                                                                                               | True         |
|  156 | true                                                  | True       | True           | ()                                                                                                                               | True         |
|  157 | false                                                 | True       | True           | ()                                                                                                                               | True         |
|  158 | NULL                                                  | False      | True           | ()                                                                                                                               | True         |
|  159 | nullptr                                               | False      | True           | ()                                                                                                                               | True         |
|  160 | comment                                               | True       | True           | ()                                                                                                                               | True         |
|  161 | translation\_unit                                     | True       | True           | ()                                                                                                                               | True         |
|  162 | \_top\_level\_item                                    | False      | False          | ()                                                                                                                               | False        |
|  163 | \_block\_item                                         | False      | False          | ()                                                                                                                               | False        |
|  164 | preproc\_include                                      | True       | True           | ()                                                                                                                               | True         |
|  165 | preproc\_def                                          | True       | True           | ()                                                                                                                               | True         |
|  166 | preproc\_function\_def                                | True       | True           | ()                                                                                                                               | True         |
|  167 | preproc\_params                                       | True       | True           | ()                                                                                                                               | True         |
|  168 | preproc\_call                                         | True       | True           | ()                                                                                                                               | True         |
|  169 | preproc\_if                                           | True       | True           | ()                                                                                                                               | True         |
|  170 | preproc\_ifdef                                        | True       | True           | ()                                                                                                                               | True         |
|  171 | preproc\_else                                         | True       | True           | ()                                                                                                                               | True         |
|  172 | preproc\_elif                                         | True       | True           | ()                                                                                                                               | True         |
|  173 | preproc\_elifdef                                      | True       | True           | ()                                                                                                                               | True         |
|  174 | preproc\_if                                           | True       | True           | ()                                                                                                                               | True         |
|  175 | preproc\_ifdef                                        | True       | True           | ()                                                                                                                               | True         |
|  176 | preproc\_else                                         | True       | True           | ()                                                                                                                               | True         |
|  177 | preproc\_elif                                         | True       | True           | ()                                                                                                                               | True         |
|  178 | preproc\_elifdef                                      | True       | True           | ()                                                                                                                               | True         |
|  179 | preproc\_if                                           | True       | True           | ()                                                                                                                               | True         |
|  180 | preproc\_ifdef                                        | True       | True           | ()                                                                                                                               | True         |
|  181 | preproc\_else                                         | True       | True           | ()                                                                                                                               | True         |
|  182 | preproc\_elif                                         | True       | True           | ()                                                                                                                               | True         |
|  183 | preproc\_elifdef                                      | True       | True           | ()                                                                                                                               | True         |
|  184 | preproc\_if                                           | True       | True           | ()                                                                                                                               | True         |
|  185 | preproc\_ifdef                                        | True       | True           | ()                                                                                                                               | True         |
|  186 | preproc\_else                                         | True       | True           | ()                                                                                                                               | True         |
|  187 | preproc\_elif                                         | True       | True           | ()                                                                                                                               | True         |
|  188 | preproc\_elifdef                                      | True       | True           | ()                                                                                                                               | True         |
|  189 | \_preproc\_expression                                 | False      | False          | ()                                                                                                                               | False        |
|  190 | parenthesized\_expression                             | True       | True           | ()                                                                                                                               | True         |
|  191 | preproc\_defined                                      | True       | True           | ()                                                                                                                               | True         |
|  192 | unary\_expression                                     | True       | True           | ()                                                                                                                               | True         |
|  193 | call\_expression                                      | True       | True           | ()                                                                                                                               | True         |
|  194 | argument\_list                                        | True       | True           | ()                                                                                                                               | True         |
|  195 | binary\_expression                                    | True       | True           | ()                                                                                                                               | True         |
|  196 | function\_definition                                  | True       | True           | ()                                                                                                                               | True         |
|  197 | function\_definition                                  | True       | True           | ()                                                                                                                               | True         |
|  198 | declaration                                           | True       | True           | ()                                                                                                                               | True         |
|  199 | type\_definition                                      | True       | True           | ()                                                                                                                               | True         |
|  200 | \_type\_definition\_type                              | False      | False          | ()                                                                                                                               | False        |
|  201 | \_type\_definition\_declarators                       | False      | False          | ()                                                                                                                               | False        |
|  202 | \_declaration\_modifiers                              | False      | False          | ()                                                                                                                               | False        |
|  203 | \_declaration\_specifiers                             | False      | False          | ()                                                                                                                               | False        |
|  204 | linkage\_specification                                | True       | True           | ()                                                                                                                               | True         |
|  205 | attribute\_specifier                                  | True       | True           | ()                                                                                                                               | True         |
|  206 | attribute                                             | True       | True           | ()                                                                                                                               | True         |
|  207 | attribute\_declaration                                | True       | True           | ()                                                                                                                               | True         |
|  208 | ms\_declspec\_modifier                                | True       | True           | ()                                                                                                                               | True         |
|  209 | ms\_based\_modifier                                   | True       | True           | ()                                                                                                                               | True         |
|  210 | ms\_call\_modifier                                    | True       | True           | ()                                                                                                                               | True         |
|  211 | ms\_unaligned\_ptr\_modifier                          | True       | True           | ()                                                                                                                               | True         |
|  212 | ms\_pointer\_modifier                                 | True       | True           | ()                                                                                                                               | True         |
|  213 | declaration\_list                                     | True       | True           | ()                                                                                                                               | True         |
|  214 | \_declarator                                          | False      | True           | (236, 223, 230, 1, 219, 226)                                                                                                     | False        |
|  215 | \_declaration\_declarator                             | False      | False          | ()                                                                                                                               | False        |
|  216 | \_field\_declarator                                   | False      | True           | (360, 231, 235, 236, 237, 238, 223, 224, 225, 230, 232, 233, 219, 220, 221, 226, 227, 228)                                       | False        |
|  217 | \_type\_declarator                                    | False      | True           | (362, 231, 235, 236, 237, 238, 223, 224, 225, 230, 232, 233, 219, 220, 221, 226, 227, 228, 93)                                   | False        |
|  218 | \_abstract\_declarator                                | False      | True           | (239, 234, 222, 229)                                                                                                             | False        |
|  219 | parenthesized\_declarator                             | True       | True           | ()                                                                                                                               | True         |
|  220 | parenthesized\_declarator                             | True       | True           | ()                                                                                                                               | True         |
|  221 | parenthesized\_declarator                             | True       | True           | ()                                                                                                                               | True         |
|  222 | abstract\_parenthesized\_declarator                   | True       | True           | ()                                                                                                                               | True         |
|  223 | attributed\_declarator                                | True       | True           | ()                                                                                                                               | True         |
|  224 | attributed\_declarator                                | True       | True           | ()                                                                                                                               | True         |
|  225 | attributed\_declarator                                | True       | True           | ()                                                                                                                               | True         |
|  226 | pointer\_declarator                                   | True       | True           | ()                                                                                                                               | True         |
|  227 | pointer\_declarator                                   | True       | True           | ()                                                                                                                               | True         |
|  228 | pointer\_declarator                                   | True       | True           | ()                                                                                                                               | True         |
|  229 | abstract\_pointer\_declarator                         | True       | True           | ()                                                                                                                               | True         |
|  230 | function\_declarator                                  | True       | True           | ()                                                                                                                               | True         |
|  231 | function\_declarator                                  | True       | True           | ()                                                                                                                               | True         |
|  232 | function\_declarator                                  | True       | True           | ()                                                                                                                               | True         |
|  233 | function\_declarator                                  | True       | True           | ()                                                                                                                               | True         |
|  234 | abstract\_function\_declarator                        | True       | True           | ()                                                                                                                               | True         |
|  235 | function\_declarator                                  | True       | True           | ()                                                                                                                               | True         |
|  236 | array\_declarator                                     | True       | True           | ()                                                                                                                               | True         |
|  237 | array\_declarator                                     | True       | True           | ()                                                                                                                               | True         |
|  238 | array\_declarator                                     | True       | True           | ()                                                                                                                               | True         |
|  239 | abstract\_array\_declarator                           | True       | True           | ()                                                                                                                               | True         |
|  240 | init\_declarator                                      | True       | True           | ()                                                                                                                               | True         |
|  241 | compound\_statement                                   | True       | True           | ()                                                                                                                               | True         |
|  242 | storage\_class\_specifier                             | True       | True           | ()                                                                                                                               | True         |
|  243 | type\_qualifier                                       | True       | True           | ()                                                                                                                               | True         |
|  244 | alignas\_qualifier                                    | True       | True           | ()                                                                                                                               | True         |
|  245 | type\_specifier                                       | False      | True           | (362, 247, 323, 93, 246, 249, 250)                                                                                               | False        |
|  246 | sized\_type\_specifier                                | True       | True           | ()                                                                                                                               | True         |
|  247 | enum\_specifier                                       | True       | True           | ()                                                                                                                               | True         |
|  248 | enumerator\_list                                      | True       | True           | ()                                                                                                                               | True         |
|  249 | struct\_specifier                                     | True       | True           | ()                                                                                                                               | True         |
|  250 | union\_specifier                                      | True       | True           | ()                                                                                                                               | True         |
|  251 | field\_declaration\_list                              | True       | True           | ()                                                                                                                               | True         |
|  252 | \_field\_declaration\_list\_item                      | False      | False          | ()                                                                                                                               | False        |
|  253 | field\_declaration                                    | True       | True           | ()                                                                                                                               | True         |
|  254 | \_field\_declaration\_declarator                      | False      | False          | ()                                                                                                                               | False        |
|  255 | bitfield\_clause                                      | True       | True           | ()                                                                                                                               | True         |
|  256 | enumerator                                            | True       | True           | ()                                                                                                                               | True         |
|  257 | variadic\_parameter                                   | True       | True           | ()                                                                                                                               | True         |
|  258 | parameter\_list                                       | True       | True           | ()                                                                                                                               | True         |
|  259 | parameter\_list                                       | True       | True           | ()                                                                                                                               | True         |
|  260 | parameter\_declaration                                | True       | True           | ()                                                                                                                               | True         |
|  261 | attributed\_statement                                 | True       | True           | ()                                                                                                                               | True         |
|  262 | statement                                             | False      | True           | (261, 276, 270, 241, 277, 272, 266, 273, 278, 267, 264, 275, 282, 279, 269, 271)                                                 | False        |
|  263 | \_top\_level\_statement                               | False      | False          | ()                                                                                                                               | False        |
|  264 | labeled\_statement                                    | True       | True           | ()                                                                                                                               | True         |
|  265 | expression\_statement                                 | True       | True           | ()                                                                                                                               | True         |
|  266 | expression\_statement                                 | True       | True           | ()                                                                                                                               | True         |
|  267 | if\_statement                                         | True       | True           | ()                                                                                                                               | True         |
|  268 | else\_clause                                          | True       | True           | ()                                                                                                                               | True         |
|  269 | switch\_statement                                     | True       | True           | ()                                                                                                                               | True         |
|  270 | case\_statement                                       | True       | True           | ()                                                                                                                               | True         |
|  271 | while\_statement                                      | True       | True           | ()                                                                                                                               | True         |
|  272 | do\_statement                                         | True       | True           | ()                                                                                                                               | True         |
|  273 | for\_statement                                        | True       | True           | ()                                                                                                                               | True         |
|  274 | \_for\_statement\_body                                | False      | False          | ()                                                                                                                               | False        |
|  275 | return\_statement                                     | True       | True           | ()                                                                                                                               | True         |
|  276 | break\_statement                                      | True       | True           | ()                                                                                                                               | True         |
|  277 | continue\_statement                                   | True       | True           | ()                                                                                                                               | True         |
|  278 | goto\_statement                                       | True       | True           | ()                                                                                                                               | True         |
|  279 | seh\_try\_statement                                   | True       | True           | ()                                                                                                                               | True         |
|  280 | seh\_except\_clause                                   | True       | True           | ()                                                                                                                               | True         |
|  281 | seh\_finally\_clause                                  | True       | True           | ()                                                                                                                               | True         |
|  282 | seh\_leave\_statement                                 | True       | True           | ()                                                                                                                               | True         |
|  283 | expression                                            | False      | True           | (295, 287, 290, 299, 292, 318, 311, 319, 286, 308, 157, 310, 297, 300, 1, 321, 141, 296, 312, 288, 294, 320, 298, 156, 289, 291) | False        |
|  284 | \_string                                              | False      | False          | ()                                                                                                                               | False        |
|  285 | comma\_expression                                     | True       | True           | ()                                                                                                                               | True         |
|  286 | conditional\_expression                               | True       | True           | ()                                                                                                                               | True         |
|  287 | assignment\_expression                                | True       | True           | ()                                                                                                                               | True         |
|  288 | pointer\_expression                                   | True       | True           | ()                                                                                                                               | True         |
|  289 | unary\_expression                                     | True       | True           | ()                                                                                                                               | True         |
|  290 | binary\_expression                                    | True       | True           | ()                                                                                                                               | True         |
|  291 | update\_expression                                    | True       | True           | ()                                                                                                                               | True         |
|  292 | cast\_expression                                      | True       | True           | ()                                                                                                                               | True         |
|  293 | type\_descriptor                                      | True       | True           | ()                                                                                                                               | True         |
|  294 | sizeof\_expression                                    | True       | True           | ()                                                                                                                               | True         |
|  295 | alignof\_expression                                   | True       | True           | ()                                                                                                                               | True         |
|  296 | offsetof\_expression                                  | True       | True           | ()                                                                                                                               | True         |
|  297 | generic\_expression                                   | True       | True           | ()                                                                                                                               | True         |
|  298 | subscript\_expression                                 | True       | True           | ()                                                                                                                               | True         |
|  299 | call\_expression                                      | True       | True           | ()                                                                                                                               | True         |
|  300 | gnu\_asm\_expression                                  | True       | True           | ()                                                                                                                               | True         |
|  301 | gnu\_asm\_qualifier                                   | True       | True           | ()                                                                                                                               | True         |
|  302 | gnu\_asm\_output\_operand\_list                       | True       | True           | ()                                                                                                                               | True         |
|  303 | gnu\_asm\_output\_operand                             | True       | True           | ()                                                                                                                               | True         |
|  304 | gnu\_asm\_input\_operand\_list                        | True       | True           | ()                                                                                                                               | True         |
|  305 | gnu\_asm\_input\_operand                              | True       | True           | ()                                                                                                                               | True         |
|  306 | gnu\_asm\_clobber\_list                               | True       | True           | ()                                                                                                                               | True         |
|  307 | gnu\_asm\_goto\_list                                  | True       | True           | ()                                                                                                                               | True         |
|  308 | extension\_expression                                 | True       | True           | ()                                                                                                                               | True         |
|  309 | argument\_list                                        | True       | True           | ()                                                                                                                               | True         |
|  310 | field\_expression                                     | True       | True           | ()                                                                                                                               | True         |
|  311 | compound\_literal\_expression                         | True       | True           | ()                                                                                                                               | True         |
|  312 | parenthesized\_expression                             | True       | True           | ()                                                                                                                               | True         |
|  313 | initializer\_list                                     | True       | True           | ()                                                                                                                               | True         |
|  314 | initializer\_pair                                     | True       | True           | ()                                                                                                                               | True         |
|  315 | subscript\_designator                                 | True       | True           | ()                                                                                                                               | True         |
|  316 | subscript\_range\_designator                          | True       | True           | ()                                                                                                                               | True         |
|  317 | field\_designator                                     | True       | True           | ()                                                                                                                               | True         |
|  318 | char\_literal                                         | True       | True           | ()                                                                                                                               | True         |
|  319 | concatenated\_string                                  | True       | True           | ()                                                                                                                               | True         |
|  320 | string\_literal                                       | True       | True           | ()                                                                                                                               | True         |
|  321 | null                                                  | True       | True           | ()                                                                                                                               | True         |
|  322 | \_empty\_declaration                                  | False      | False          | ()                                                                                                                               | False        |
|  323 | macro\_type\_specifier                                | True       | True           | ()                                                                                                                               | True         |
|  324 | translation\_unit\_repeat1                            | False      | False          | ()                                                                                                                               | False        |
|  325 | preproc\_params\_repeat1                              | False      | False          | ()                                                                                                                               | False        |
|  326 | preproc\_if\_repeat1                                  | False      | False          | ()                                                                                                                               | False        |
|  327 | preproc\_if\_in\_field\_declaration\_list\_repeat1    | False      | False          | ()                                                                                                                               | False        |
|  328 | preproc\_if\_in\_enumerator\_list\_repeat1            | False      | False          | ()                                                                                                                               | False        |
|  329 | preproc\_if\_in\_enumerator\_list\_no\_comma\_repeat1 | False      | False          | ()                                                                                                                               | False        |
|  330 | preproc\_argument\_list\_repeat1                      | False      | False          | ()                                                                                                                               | False        |
|  331 | \_old\_style\_function\_definition\_repeat1           | False      | False          | ()                                                                                                                               | False        |
|  332 | declaration\_repeat1                                  | False      | False          | ()                                                                                                                               | False        |
|  333 | type\_definition\_repeat1                             | False      | False          | ()                                                                                                                               | False        |
|  334 | \_type\_definition\_type\_repeat1                     | False      | False          | ()                                                                                                                               | False        |
|  335 | \_type\_definition\_declarators\_repeat1              | False      | False          | ()                                                                                                                               | False        |
|  336 | \_declaration\_specifiers\_repeat1                    | False      | False          | ()                                                                                                                               | False        |
|  337 | attribute\_declaration\_repeat1                       | False      | False          | ()                                                                                                                               | False        |
|  338 | attributed\_declarator\_repeat1                       | False      | False          | ()                                                                                                                               | False        |
|  339 | pointer\_declarator\_repeat1                          | False      | False          | ()                                                                                                                               | False        |
|  340 | function\_declarator\_repeat1                         | False      | False          | ()                                                                                                                               | False        |
|  341 | array\_declarator\_repeat1                            | False      | False          | ()                                                                                                                               | False        |
|  342 | sized\_type\_specifier\_repeat1                       | False      | False          | ()                                                                                                                               | False        |
|  343 | enumerator\_list\_repeat1                             | False      | False          | ()                                                                                                                               | False        |
|  344 | \_field\_declaration\_declarator\_repeat1             | False      | False          | ()                                                                                                                               | False        |
|  345 | parameter\_list\_repeat1                              | False      | False          | ()                                                                                                                               | False        |
|  346 | \_old\_style\_parameter\_list\_repeat1                | False      | False          | ()                                                                                                                               | False        |
|  347 | case\_statement\_repeat1                              | False      | False          | ()                                                                                                                               | False        |
|  348 | generic\_expression\_repeat1                          | False      | False          | ()                                                                                                                               | False        |
|  349 | gnu\_asm\_expression\_repeat1                         | False      | False          | ()                                                                                                                               | False        |
|  350 | gnu\_asm\_output\_operand\_list\_repeat1              | False      | False          | ()                                                                                                                               | False        |
|  351 | gnu\_asm\_input\_operand\_list\_repeat1               | False      | False          | ()                                                                                                                               | False        |
|  352 | gnu\_asm\_clobber\_list\_repeat1                      | False      | False          | ()                                                                                                                               | False        |
|  353 | gnu\_asm\_goto\_list\_repeat1                         | False      | False          | ()                                                                                                                               | False        |
|  354 | argument\_list\_repeat1                               | False      | False          | ()                                                                                                                               | False        |
|  355 | initializer\_list\_repeat1                            | False      | False          | ()                                                                                                                               | False        |
|  356 | initializer\_pair\_repeat1                            | False      | False          | ()                                                                                                                               | False        |
|  357 | char\_literal\_repeat1                                | False      | False          | ()                                                                                                                               | False        |
|  358 | concatenated\_string\_repeat1                         | False      | False          | ()                                                                                                                               | False        |
|  359 | string\_literal\_repeat1                              | False      | False          | ()                                                                                                                               | False        |
|  360 | field\_identifier                                     | True       | True           | ()                                                                                                                               | True         |
|  361 | statement\_identifier                                 | True       | True           | ()                                                                                                                               | True         |
|  362 | type\_identifier                                      | True       | True           | ()                                                                                                                               | True         |

## Fields

|   id | name             |
|------|------------------|
|    0 | `None`           |
|    1 | alternative      |
|    2 | argument         |
|    3 | arguments        |
|    4 | assembly\_code   |
|    5 | body             |
|    6 | clobbers         |
|    7 | condition        |
|    8 | consequence      |
|    9 | constraint       |
|   10 | declarator       |
|   11 | designator       |
|   12 | directive        |
|   13 | end              |
|   14 | field            |
|   15 | filter           |
|   16 | function         |
|   17 | goto\_labels     |
|   18 | index            |
|   19 | initializer      |
|   20 | input\_operands  |
|   21 | label            |
|   22 | left             |
|   23 | member           |
|   24 | name             |
|   25 | operand          |
|   26 | operator         |
|   27 | output\_operands |
|   28 | parameters       |
|   29 | path             |
|   30 | prefix           |
|   31 | register         |
|   32 | right            |
|   33 | size             |
|   34 | start            |
|   35 | symbol           |
|   36 | type             |
|   37 | underlying\_type |
|   38 | update           |


# CPP

- Language: cpp
- ABI version: 14
- File name extensions: ['.cpp', '.hpp', '.cc', '.cxx', '.hh', '.hxx']
- File name patterns: []
- Node kinds count: 543
    - Anonymous node count: 287
    - Visible node count: 452
    - Supertype node count: 459
- Field count: 50

## Node kinds

|   id | name                                                  | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|-------------------------------------------------------|------------|----------------|---------------|--------------|
|    0 | end                                                   | False      | False          | ()            | False        |
|    1 | identifier                                            | True       | True           | ()            | True         |
|    2 | #include                                              | False      | True           | ()            | True         |
|    3 | preproc\_include\_token2                              | False      | False          | ()            | False        |
|    4 | #define                                               | False      | True           | ()            | True         |
|    5 | (                                                     | False      | True           | ()            | True         |
|    6 | ...                                                   | False      | True           | ()            | True         |
|    7 | ,                                                     | False      | True           | ()            | True         |
|    8 | )                                                     | False      | True           | ()            | True         |
|    9 | #if                                                   | False      | True           | ()            | True         |
|   10 |                                                       | False      | True           | ()            | True         |
|   11 | #endif                                                | False      | True           | ()            | True         |
|   12 | #ifdef                                                | False      | True           | ()            | True         |
|   13 | #ifndef                                               | False      | True           | ()            | True         |
|   14 | #else                                                 | False      | True           | ()            | True         |
|   15 | #elif                                                 | False      | True           | ()            | True         |
|   16 | #elifdef                                              | False      | True           | ()            | True         |
|   17 | #elifndef                                             | False      | True           | ()            | True         |
|   18 | preproc\_arg                                          | True       | True           | ()            | True         |
|   19 | preproc\_directive                                    | True       | True           | ()            | True         |
|   20 | (                                                     | False      | True           | ()            | True         |
|   21 | defined                                               | False      | True           | ()            | True         |
|   22 | !                                                     | False      | True           | ()            | True         |
|   23 | ~                                                     | False      | True           | ()            | True         |
|   24 | -                                                     | False      | True           | ()            | True         |
|   25 | +                                                     | False      | True           | ()            | True         |
|   26 | \*                                                    | False      | True           | ()            | True         |
|   27 | /                                                     | False      | True           | ()            | True         |
|   28 | %                                                     | False      | True           | ()            | True         |
|   29 | &#124;&#124;                                          | False      | True           | ()            | True         |
|   30 | &amp;&amp;                                            | False      | True           | ()            | True         |
|   31 | &#124;                                                | False      | True           | ()            | True         |
|   32 | ^                                                     | False      | True           | ()            | True         |
|   33 | &amp;                                                 | False      | True           | ()            | True         |
|   34 | ==                                                    | False      | True           | ()            | True         |
|   35 | !=                                                    | False      | True           | ()            | True         |
|   36 | &gt;                                                  | False      | True           | ()            | True         |
|   37 | &gt;=                                                 | False      | True           | ()            | True         |
|   38 | &lt;=                                                 | False      | True           | ()            | True         |
|   39 | &lt;                                                  | False      | True           | ()            | True         |
|   40 | &lt;&lt;                                              | False      | True           | ()            | True         |
|   41 | &gt;&gt;                                              | False      | True           | ()            | True         |
|   42 | ;                                                     | False      | True           | ()            | True         |
|   43 | \_\_extension\_\_                                     | False      | True           | ()            | True         |
|   44 | typedef                                               | False      | True           | ()            | True         |
|   45 | virtual                                               | False      | True           | ()            | True         |
|   46 | extern                                                | False      | True           | ()            | True         |
|   47 | \_\_attribute\_\_                                     | False      | True           | ()            | True         |
|   48 | \_\_attribute                                         | False      | True           | ()            | True         |
|   49 | ::                                                    | False      | True           | ()            | True         |
|   50 | [[                                                    | False      | True           | ()            | True         |
|   51 | ]]                                                    | False      | True           | ()            | True         |
|   52 | \_\_declspec                                          | False      | True           | ()            | True         |
|   53 | \_\_based                                             | False      | True           | ()            | True         |
|   54 | \_\_cdecl                                             | False      | True           | ()            | True         |
|   55 | \_\_clrcall                                           | False      | True           | ()            | True         |
|   56 | \_\_stdcall                                           | False      | True           | ()            | True         |
|   57 | \_\_fastcall                                          | False      | True           | ()            | True         |
|   58 | \_\_thiscall                                          | False      | True           | ()            | True         |
|   59 | \_\_vectorcall                                        | False      | True           | ()            | True         |
|   60 | ms\_restrict\_modifier                                | True       | True           | ()            | True         |
|   61 | ms\_unsigned\_ptr\_modifier                           | True       | True           | ()            | True         |
|   62 | ms\_signed\_ptr\_modifier                             | True       | True           | ()            | True         |
|   63 | \_unaligned                                           | False      | True           | ()            | True         |
|   64 | \_\_unaligned                                         | False      | True           | ()            | True         |
|   65 | {                                                     | False      | True           | ()            | True         |
|   66 | }                                                     | False      | True           | ()            | True         |
|   67 | signed                                                | False      | True           | ()            | True         |
|   68 | unsigned                                              | False      | True           | ()            | True         |
|   69 | long                                                  | False      | True           | ()            | True         |
|   70 | short                                                 | False      | True           | ()            | True         |
|   71 | [                                                     | False      | True           | ()            | True         |
|   72 | static                                                | False      | True           | ()            | True         |
|   73 | ]                                                     | False      | True           | ()            | True         |
|   74 | =                                                     | False      | True           | ()            | True         |
|   75 | register                                              | False      | True           | ()            | True         |
|   76 | inline                                                | False      | True           | ()            | True         |
|   77 | \_\_inline                                            | False      | True           | ()            | True         |
|   78 | \_\_inline\_\_                                        | False      | True           | ()            | True         |
|   79 | \_\_forceinline                                       | False      | True           | ()            | True         |
|   80 | thread\_local                                         | False      | True           | ()            | True         |
|   81 | \_\_thread                                            | False      | True           | ()            | True         |
|   82 | const                                                 | False      | True           | ()            | True         |
|   83 | constexpr                                             | False      | True           | ()            | True         |
|   84 | volatile                                              | False      | True           | ()            | True         |
|   85 | restrict                                              | False      | True           | ()            | True         |
|   86 | \_\_restrict\_\_                                      | False      | True           | ()            | True         |
|   87 | \_Atomic                                              | False      | True           | ()            | True         |
|   88 | \_Noreturn                                            | False      | True           | ()            | True         |
|   89 | noreturn                                              | False      | True           | ()            | True         |
|   90 | \_Nonnull                                             | False      | True           | ()            | True         |
|   91 | mutable                                               | False      | True           | ()            | True         |
|   92 | constinit                                             | False      | True           | ()            | True         |
|   93 | consteval                                             | False      | True           | ()            | True         |
|   94 | alignas                                               | False      | True           | ()            | True         |
|   95 | \_Alignas                                             | False      | True           | ()            | True         |
|   96 | primitive\_type                                       | True       | True           | ()            | True         |
|   97 | enum                                                  | False      | True           | ()            | True         |
|   98 | class                                                 | False      | True           | ()            | True         |
|   99 | struct                                                | False      | True           | ()            | True         |
|  100 | union                                                 | False      | True           | ()            | True         |
|  101 | :                                                     | False      | True           | ()            | True         |
|  102 | if                                                    | False      | True           | ()            | True         |
|  103 | else                                                  | False      | True           | ()            | True         |
|  104 | switch                                                | False      | True           | ()            | True         |
|  105 | case                                                  | False      | True           | ()            | True         |
|  106 | default                                               | False      | True           | ()            | True         |
|  107 | while                                                 | False      | True           | ()            | True         |
|  108 | do                                                    | False      | True           | ()            | True         |
|  109 | for                                                   | False      | True           | ()            | True         |
|  110 | return                                                | False      | True           | ()            | True         |
|  111 | break                                                 | False      | True           | ()            | True         |
|  112 | continue                                              | False      | True           | ()            | True         |
|  113 | goto                                                  | False      | True           | ()            | True         |
|  114 | \_\_try                                               | False      | True           | ()            | True         |
|  115 | \_\_except                                            | False      | True           | ()            | True         |
|  116 | \_\_finally                                           | False      | True           | ()            | True         |
|  117 | \_\_leave                                             | False      | True           | ()            | True         |
|  118 | ?                                                     | False      | True           | ()            | True         |
|  119 | \*=                                                   | False      | True           | ()            | True         |
|  120 | /=                                                    | False      | True           | ()            | True         |
|  121 | %=                                                    | False      | True           | ()            | True         |
|  122 | +=                                                    | False      | True           | ()            | True         |
|  123 | -=                                                    | False      | True           | ()            | True         |
|  124 | &lt;&lt;=                                             | False      | True           | ()            | True         |
|  125 | &gt;&gt;=                                             | False      | True           | ()            | True         |
|  126 | &amp;=                                                | False      | True           | ()            | True         |
|  127 | ^=                                                    | False      | True           | ()            | True         |
|  128 | &#124;=                                               | False      | True           | ()            | True         |
|  129 | and\_eq                                               | False      | True           | ()            | True         |
|  130 | or\_eq                                                | False      | True           | ()            | True         |
|  131 | xor\_eq                                               | False      | True           | ()            | True         |
|  132 | not                                                   | False      | True           | ()            | True         |
|  133 | compl                                                 | False      | True           | ()            | True         |
|  134 | &lt;=&gt;                                             | False      | True           | ()            | True         |
|  135 | or                                                    | False      | True           | ()            | True         |
|  136 | and                                                   | False      | True           | ()            | True         |
|  137 | bitor                                                 | False      | True           | ()            | True         |
|  138 | xor                                                   | False      | True           | ()            | True         |
|  139 | bitand                                                | False      | True           | ()            | True         |
|  140 | not\_eq                                               | False      | True           | ()            | True         |
|  141 | --                                                    | False      | True           | ()            | True         |
|  142 | ++                                                    | False      | True           | ()            | True         |
|  143 | sizeof                                                | False      | True           | ()            | True         |
|  144 | \_\_alignof\_\_                                       | False      | True           | ()            | True         |
|  145 | \_\_alignof                                           | False      | True           | ()            | True         |
|  146 | \_alignof                                             | False      | True           | ()            | True         |
|  147 | alignof                                               | False      | True           | ()            | True         |
|  148 | \_Alignof                                             | False      | True           | ()            | True         |
|  149 | offsetof                                              | False      | True           | ()            | True         |
|  150 | \_Generic                                             | False      | True           | ()            | True         |
|  151 | asm                                                   | False      | True           | ()            | True         |
|  152 | \_\_asm\_\_                                           | False      | True           | ()            | True         |
|  153 | \_\_asm                                               | False      | True           | ()            | True         |
|  154 | \_\_volatile\_\_                                      | False      | True           | ()            | True         |
|  155 | .                                                     | False      | True           | ()            | True         |
|  156 | .\*                                                   | False      | True           | ()            | True         |
|  157 | -&gt;                                                 | False      | True           | ()            | True         |
|  158 | number\_literal                                       | True       | True           | ()            | True         |
|  159 | L'                                                    | False      | True           | ()            | True         |
|  160 | u'                                                    | False      | True           | ()            | True         |
|  161 | U'                                                    | False      | True           | ()            | True         |
|  162 | u8'                                                   | False      | True           | ()            | True         |
|  163 | '                                                     | False      | True           | ()            | True         |
|  164 | character                                             | True       | True           | ()            | True         |
|  165 | L"                                                    | False      | True           | ()            | True         |
|  166 | u"                                                    | False      | True           | ()            | True         |
|  167 | U"                                                    | False      | True           | ()            | True         |
|  168 | u8"                                                   | False      | True           | ()            | True         |
|  169 | "                                                     | False      | True           | ()            | True         |
|  170 | string\_content                                       | True       | True           | ()            | True         |
|  171 | escape\_sequence                                      | True       | True           | ()            | True         |
|  172 | system\_lib\_string                                   | True       | True           | ()            | True         |
|  173 | true                                                  | True       | True           | ()            | True         |
|  174 | false                                                 | True       | True           | ()            | True         |
|  175 | NULL                                                  | False      | True           | ()            | True         |
|  176 | nullptr                                               | False      | True           | ()            | True         |
|  177 | comment                                               | True       | True           | ()            | True         |
|  178 | auto                                                  | True       | True           | ()            | True         |
|  179 | decltype                                              | False      | True           | ()            | True         |
|  180 | final                                                 | False      | True           | ()            | True         |
|  181 | override                                              | False      | True           | ()            | True         |
|  182 | explicit                                              | False      | True           | ()            | True         |
|  183 | typename                                              | False      | True           | ()            | True         |
|  184 | template                                              | False      | True           | ()            | True         |
|  185 | &gt;                                                  | False      | True           | ()            | True         |
|  186 | operator                                              | False      | True           | ()            | True         |
|  187 | try                                                   | False      | True           | ()            | True         |
|  188 | delete                                                | False      | True           | ()            | True         |
|  189 | pure\_virtual\_clause\_token1                         | False      | False          | ()            | False        |
|  190 | friend                                                | False      | True           | ()            | True         |
|  191 | public                                                | False      | True           | ()            | True         |
|  192 | private                                               | False      | True           | ()            | True         |
|  193 | protected                                             | False      | True           | ()            | True         |
|  194 | noexcept                                              | False      | True           | ()            | True         |
|  195 | throw                                                 | False      | True           | ()            | True         |
|  196 | namespace                                             | False      | True           | ()            | True         |
|  197 | using                                                 | False      | True           | ()            | True         |
|  198 | static\_assert                                        | False      | True           | ()            | True         |
|  199 | concept                                               | False      | True           | ()            | True         |
|  200 | co\_return                                            | False      | True           | ()            | True         |
|  201 | co\_yield                                             | False      | True           | ()            | True         |
|  202 | catch                                                 | False      | True           | ()            | True         |
|  203 | R"                                                    | False      | True           | ()            | True         |
|  204 | LR"                                                   | False      | True           | ()            | True         |
|  205 | uR"                                                   | False      | True           | ()            | True         |
|  206 | UR"                                                   | False      | True           | ()            | True         |
|  207 | u8R"                                                  | False      | True           | ()            | True         |
|  208 | co\_await                                             | False      | True           | ()            | True         |
|  209 | new                                                   | False      | True           | ()            | True         |
|  210 | requires                                              | False      | True           | ()            | True         |
|  211 | -&gt;\*                                               | False      | True           | ()            | True         |
|  212 | ()                                                    | False      | True           | ()            | True         |
|  213 | []                                                    | False      | True           | ()            | True         |
|  214 | ""                                                    | False      | True           | ()            | True         |
|  215 | this                                                  | True       | True           | ()            | True         |
|  216 | literal\_suffix                                       | True       | True           | ()            | True         |
|  217 | raw\_string\_delimiter                                | True       | True           | ()            | True         |
|  218 | raw\_string\_content                                  | True       | True           | ()            | True         |
|  219 | translation\_unit                                     | True       | True           | ()            | True         |
|  220 | \_top\_level\_item                                    | False      | False          | ()            | False        |
|  221 | \_block\_item                                         | False      | False          | ()            | False        |
|  222 | preproc\_include                                      | True       | True           | ()            | True         |
|  223 | preproc\_def                                          | True       | True           | ()            | True         |
|  224 | preproc\_function\_def                                | True       | True           | ()            | True         |
|  225 | preproc\_params                                       | True       | True           | ()            | True         |
|  226 | preproc\_call                                         | True       | True           | ()            | True         |
|  227 | preproc\_if                                           | True       | True           | ()            | True         |
|  228 | preproc\_ifdef                                        | True       | True           | ()            | True         |
|  229 | preproc\_else                                         | True       | True           | ()            | True         |
|  230 | preproc\_elif                                         | True       | True           | ()            | True         |
|  231 | preproc\_elifdef                                      | True       | True           | ()            | True         |
|  232 | preproc\_if                                           | True       | True           | ()            | True         |
|  233 | preproc\_ifdef                                        | True       | True           | ()            | True         |
|  234 | preproc\_else                                         | True       | True           | ()            | True         |
|  235 | preproc\_elif                                         | True       | True           | ()            | True         |
|  236 | preproc\_elifdef                                      | True       | True           | ()            | True         |
|  237 | preproc\_if                                           | True       | True           | ()            | True         |
|  238 | preproc\_ifdef                                        | True       | True           | ()            | True         |
|  239 | preproc\_else                                         | True       | True           | ()            | True         |
|  240 | preproc\_elif                                         | True       | True           | ()            | True         |
|  241 | preproc\_elifdef                                      | True       | True           | ()            | True         |
|  242 | preproc\_if                                           | True       | True           | ()            | True         |
|  243 | preproc\_ifdef                                        | True       | True           | ()            | True         |
|  244 | preproc\_else                                         | True       | True           | ()            | True         |
|  245 | preproc\_elif                                         | True       | True           | ()            | True         |
|  246 | preproc\_elifdef                                      | True       | True           | ()            | True         |
|  247 | \_preproc\_expression                                 | False      | False          | ()            | False        |
|  248 | parenthesized\_expression                             | True       | True           | ()            | True         |
|  249 | preproc\_defined                                      | True       | True           | ()            | True         |
|  250 | unary\_expression                                     | True       | True           | ()            | True         |
|  251 | call\_expression                                      | True       | True           | ()            | True         |
|  252 | argument\_list                                        | True       | True           | ()            | True         |
|  253 | binary\_expression                                    | True       | True           | ()            | True         |
|  254 | function\_definition                                  | True       | True           | ()            | True         |
|  255 | declaration                                           | True       | True           | ()            | True         |
|  256 | type\_definition                                      | True       | True           | ()            | True         |
|  257 | \_type\_definition\_type                              | False      | False          | ()            | False        |
|  258 | \_type\_definition\_declarators                       | False      | False          | ()            | False        |
|  259 | \_declaration\_modifiers                              | False      | False          | ()            | False        |
|  260 | \_declaration\_specifiers                             | False      | False          | ()            | False        |
|  261 | linkage\_specification                                | True       | True           | ()            | True         |
|  262 | attribute\_specifier                                  | True       | True           | ()            | True         |
|  263 | attribute                                             | True       | True           | ()            | True         |
|  264 | attribute\_declaration                                | True       | True           | ()            | True         |
|  265 | ms\_declspec\_modifier                                | True       | True           | ()            | True         |
|  266 | ms\_based\_modifier                                   | True       | True           | ()            | True         |
|  267 | ms\_call\_modifier                                    | True       | True           | ()            | True         |
|  268 | ms\_unaligned\_ptr\_modifier                          | True       | True           | ()            | True         |
|  269 | ms\_pointer\_modifier                                 | True       | True           | ()            | True         |
|  270 | declaration\_list                                     | True       | True           | ()            | True         |
|  271 | \_declarator                                          | False      | True           | ()            | False        |
|  272 | \_field\_declarator                                   | False      | True           | ()            | False        |
|  273 | \_type\_declarator                                    | False      | True           | ()            | False        |
|  274 | \_abstract\_declarator                                | False      | True           | ()            | False        |
|  275 | parenthesized\_declarator                             | True       | True           | ()            | True         |
|  276 | parenthesized\_declarator                             | True       | True           | ()            | True         |
|  277 | parenthesized\_declarator                             | True       | True           | ()            | True         |
|  278 | abstract\_parenthesized\_declarator                   | True       | True           | ()            | True         |
|  279 | attributed\_declarator                                | True       | True           | ()            | True         |
|  280 | attributed\_declarator                                | True       | True           | ()            | True         |
|  281 | attributed\_declarator                                | True       | True           | ()            | True         |
|  282 | pointer\_declarator                                   | True       | True           | ()            | True         |
|  283 | pointer\_declarator                                   | True       | True           | ()            | True         |
|  284 | pointer\_type\_declarator                             | True       | True           | ()            | True         |
|  285 | abstract\_pointer\_declarator                         | True       | True           | ()            | True         |
|  286 | function\_declarator                                  | True       | True           | ()            | True         |
|  287 | function\_declarator                                  | True       | True           | ()            | True         |
|  288 | function\_declarator                                  | True       | True           | ()            | True         |
|  289 | abstract\_function\_declarator                        | True       | True           | ()            | True         |
|  290 | array\_declarator                                     | True       | True           | ()            | True         |
|  291 | array\_declarator                                     | True       | True           | ()            | True         |
|  292 | array\_declarator                                     | True       | True           | ()            | True         |
|  293 | abstract\_array\_declarator                           | True       | True           | ()            | True         |
|  294 | init\_declarator                                      | True       | True           | ()            | True         |
|  295 | compound\_statement                                   | True       | True           | ()            | True         |
|  296 | storage\_class\_specifier                             | True       | True           | ()            | True         |
|  297 | type\_qualifier                                       | True       | True           | ()            | True         |
|  298 | alignas\_qualifier                                    | True       | True           | ()            | True         |
|  299 | type\_specifier                                       | False      | True           | ()            | False        |
|  300 | sized\_type\_specifier                                | True       | True           | ()            | True         |
|  301 | enum\_specifier                                       | True       | True           | ()            | True         |
|  302 | enumerator\_list                                      | True       | True           | ()            | True         |
|  303 | struct\_specifier                                     | True       | True           | ()            | True         |
|  304 | union\_specifier                                      | True       | True           | ()            | True         |
|  305 | field\_declaration\_list                              | True       | True           | ()            | True         |
|  306 | \_field\_declaration\_list\_item                      | False      | False          | ()            | False        |
|  307 | field\_declaration                                    | True       | True           | ()            | True         |
|  308 | bitfield\_clause                                      | True       | True           | ()            | True         |
|  309 | enumerator                                            | True       | True           | ()            | True         |
|  310 | parameter\_list                                       | True       | True           | ()            | True         |
|  311 | parameter\_declaration                                | True       | True           | ()            | True         |
|  312 | attributed\_statement                                 | True       | True           | ()            | True         |
|  313 | statement                                             | False      | True           | ()            | False        |
|  314 | \_top\_level\_statement                               | False      | False          | ()            | False        |
|  315 | labeled\_statement                                    | True       | True           | ()            | True         |
|  316 | expression\_statement                                 | True       | True           | ()            | True         |
|  317 | expression\_statement                                 | True       | True           | ()            | True         |
|  318 | if\_statement                                         | True       | True           | ()            | True         |
|  319 | else\_clause                                          | True       | True           | ()            | True         |
|  320 | switch\_statement                                     | True       | True           | ()            | True         |
|  321 | case\_statement                                       | True       | True           | ()            | True         |
|  322 | while\_statement                                      | True       | True           | ()            | True         |
|  323 | do\_statement                                         | True       | True           | ()            | True         |
|  324 | for\_statement                                        | True       | True           | ()            | True         |
|  325 | \_for\_statement\_body                                | False      | False          | ()            | False        |
|  326 | return\_statement                                     | True       | True           | ()            | True         |
|  327 | break\_statement                                      | True       | True           | ()            | True         |
|  328 | continue\_statement                                   | True       | True           | ()            | True         |
|  329 | goto\_statement                                       | True       | True           | ()            | True         |
|  330 | seh\_try\_statement                                   | True       | True           | ()            | True         |
|  331 | seh\_except\_clause                                   | True       | True           | ()            | True         |
|  332 | seh\_finally\_clause                                  | True       | True           | ()            | True         |
|  333 | seh\_leave\_statement                                 | True       | True           | ()            | True         |
|  334 | expression                                            | False      | True           | ()            | False        |
|  335 | \_string                                              | False      | False          | ()            | False        |
|  336 | comma\_expression                                     | True       | True           | ()            | True         |
|  337 | conditional\_expression                               | True       | True           | ()            | True         |
|  338 | assignment\_expression                                | True       | True           | ()            | True         |
|  339 | pointer\_expression                                   | True       | True           | ()            | True         |
|  340 | unary\_expression                                     | True       | True           | ()            | True         |
|  341 | binary\_expression                                    | True       | True           | ()            | True         |
|  342 | update\_expression                                    | True       | True           | ()            | True         |
|  343 | cast\_expression                                      | True       | True           | ()            | True         |
|  344 | type\_descriptor                                      | True       | True           | ()            | True         |
|  345 | sizeof\_expression                                    | True       | True           | ()            | True         |
|  346 | alignof\_expression                                   | True       | True           | ()            | True         |
|  347 | offsetof\_expression                                  | True       | True           | ()            | True         |
|  348 | generic\_expression                                   | True       | True           | ()            | True         |
|  349 | subscript\_expression                                 | True       | True           | ()            | True         |
|  350 | call\_expression                                      | True       | True           | ()            | True         |
|  351 | gnu\_asm\_expression                                  | True       | True           | ()            | True         |
|  352 | gnu\_asm\_qualifier                                   | True       | True           | ()            | True         |
|  353 | gnu\_asm\_output\_operand\_list                       | True       | True           | ()            | True         |
|  354 | gnu\_asm\_output\_operand                             | True       | True           | ()            | True         |
|  355 | gnu\_asm\_input\_operand\_list                        | True       | True           | ()            | True         |
|  356 | gnu\_asm\_input\_operand                              | True       | True           | ()            | True         |
|  357 | gnu\_asm\_clobber\_list                               | True       | True           | ()            | True         |
|  358 | gnu\_asm\_goto\_list                                  | True       | True           | ()            | True         |
|  359 | extension\_expression                                 | True       | True           | ()            | True         |
|  360 | argument\_list                                        | True       | True           | ()            | True         |
|  361 | field\_expression                                     | True       | True           | ()            | True         |
|  362 | compound\_literal\_expression                         | True       | True           | ()            | True         |
|  363 | parenthesized\_expression                             | True       | True           | ()            | True         |
|  364 | initializer\_list                                     | True       | True           | ()            | True         |
|  365 | initializer\_pair                                     | True       | True           | ()            | True         |
|  366 | subscript\_designator                                 | True       | True           | ()            | True         |
|  367 | subscript\_range\_designator                          | True       | True           | ()            | True         |
|  368 | field\_designator                                     | True       | True           | ()            | True         |
|  369 | char\_literal                                         | True       | True           | ()            | True         |
|  370 | concatenated\_string                                  | True       | True           | ()            | True         |
|  371 | string\_literal                                       | True       | True           | ()            | True         |
|  372 | null                                                  | True       | True           | ()            | True         |
|  373 | \_empty\_declaration                                  | False      | False          | ()            | False        |
|  374 | placeholder\_type\_specifier                          | True       | True           | ()            | True         |
|  375 | decltype                                              | True       | True           | ()            | True         |
|  376 | decltype                                              | True       | True           | ()            | True         |
|  377 | \_class\_declaration                                  | False      | False          | ()            | False        |
|  378 | \_class\_declaration\_item                            | False      | False          | ()            | False        |
|  379 | class\_specifier                                      | True       | True           | ()            | True         |
|  380 | \_class\_name                                         | False      | False          | ()            | False        |
|  381 | virtual\_specifier                                    | True       | True           | ()            | True         |
|  382 | explicit\_function\_specifier                         | True       | True           | ()            | True         |
|  383 | base\_class\_clause                                   | True       | True           | ()            | True         |
|  384 | \_enum\_base\_clause                                  | False      | False          | ()            | False        |
|  385 | dependent\_type                                       | True       | True           | ()            | True         |
|  386 | template\_declaration                                 | True       | True           | ()            | True         |
|  387 | template\_instantiation                               | True       | True           | ()            | True         |
|  388 | template\_parameter\_list                             | True       | True           | ()            | True         |
|  389 | type\_parameter\_declaration                          | True       | True           | ()            | True         |
|  390 | variadic\_type\_parameter\_declaration                | True       | True           | ()            | True         |
|  391 | optional\_type\_parameter\_declaration                | True       | True           | ()            | True         |
|  392 | template\_template\_parameter\_declaration            | True       | True           | ()            | True         |
|  393 | optional\_parameter\_declaration                      | True       | True           | ()            | True         |
|  394 | variadic\_parameter\_declaration                      | True       | True           | ()            | True         |
|  395 | variadic\_declarator                                  | True       | True           | ()            | True         |
|  396 | reference\_declarator                                 | True       | True           | ()            | True         |
|  397 | operator\_cast                                        | True       | True           | ()            | True         |
|  398 | field\_initializer\_list                              | True       | True           | ()            | True         |
|  399 | field\_initializer                                    | True       | True           | ()            | True         |
|  400 | function\_definition                                  | True       | True           | ()            | True         |
|  401 | \_constructor\_specifiers                             | False      | False          | ()            | False        |
|  402 | function\_definition                                  | True       | True           | ()            | True         |
|  403 | declaration                                           | True       | True           | ()            | True         |
|  404 | try\_statement                                        | True       | True           | ()            | True         |
|  405 | function\_definition                                  | True       | True           | ()            | True         |
|  406 | declaration                                           | True       | True           | ()            | True         |
|  407 | default\_method\_clause                               | True       | True           | ()            | True         |
|  408 | delete\_method\_clause                                | True       | True           | ()            | True         |
|  409 | pure\_virtual\_clause                                 | True       | True           | ()            | True         |
|  410 | friend\_declaration                                   | True       | True           | ()            | True         |
|  411 | access\_specifier                                     | True       | True           | ()            | True         |
|  412 | reference\_declarator                                 | True       | True           | ()            | True         |
|  413 | reference\_declarator                                 | True       | True           | ()            | True         |
|  414 | reference\_declarator                                 | True       | True           | ()            | True         |
|  415 | abstract\_reference\_declarator                       | True       | True           | ()            | True         |
|  416 | structured\_binding\_declarator                       | True       | True           | ()            | True         |
|  417 | ref\_qualifier                                        | True       | True           | ()            | True         |
|  418 | \_function\_declarator\_seq                           | False      | False          | ()            | False        |
|  419 | \_function\_attributes\_start                         | False      | False          | ()            | False        |
|  420 | \_function\_exception\_specification                  | False      | False          | ()            | False        |
|  421 | \_function\_attributes\_end                           | False      | False          | ()            | False        |
|  422 | \_function\_postfix                                   | False      | False          | ()            | False        |
|  423 | trailing\_return\_type                                | True       | True           | ()            | True         |
|  424 | noexcept                                              | True       | True           | ()            | True         |
|  425 | throw\_specifier                                      | True       | True           | ()            | True         |
|  426 | template\_type                                        | True       | True           | ()            | True         |
|  427 | template\_method                                      | True       | True           | ()            | True         |
|  428 | template\_function                                    | True       | True           | ()            | True         |
|  429 | template\_argument\_list                              | True       | True           | ()            | True         |
|  430 | namespace\_definition                                 | True       | True           | ()            | True         |
|  431 | namespace\_alias\_definition                          | True       | True           | ()            | True         |
|  432 | \_namespace\_specifier                                | False      | False          | ()            | False        |
|  433 | nested\_namespace\_specifier                          | True       | True           | ()            | True         |
|  434 | using\_declaration                                    | True       | True           | ()            | True         |
|  435 | alias\_declaration                                    | True       | True           | ()            | True         |
|  436 | static\_assert\_declaration                           | True       | True           | ()            | True         |
|  437 | concept\_definition                                   | True       | True           | ()            | True         |
|  438 | for\_range\_loop                                      | True       | True           | ()            | True         |
|  439 | \_for\_range\_loop\_body                              | False      | False          | ()            | False        |
|  440 | init\_statement                                       | True       | True           | ()            | True         |
|  441 | condition\_clause                                     | True       | True           | ()            | True         |
|  442 | declaration                                           | True       | True           | ()            | True         |
|  443 | co\_return\_statement                                 | True       | True           | ()            | True         |
|  444 | co\_yield\_statement                                  | True       | True           | ()            | True         |
|  445 | throw\_statement                                      | True       | True           | ()            | True         |
|  446 | try\_statement                                        | True       | True           | ()            | True         |
|  447 | catch\_clause                                         | True       | True           | ()            | True         |
|  448 | raw\_string\_literal                                  | True       | True           | ()            | True         |
|  449 | subscript\_argument\_list                             | True       | True           | ()            | True         |
|  450 | co\_await\_expression                                 | True       | True           | ()            | True         |
|  451 | new\_expression                                       | True       | True           | ()            | True         |
|  452 | new\_declarator                                       | True       | True           | ()            | True         |
|  453 | delete\_expression                                    | True       | True           | ()            | True         |
|  454 | type\_requirement                                     | True       | True           | ()            | True         |
|  455 | compound\_requirement                                 | True       | True           | ()            | True         |
|  456 | \_requirement                                         | False      | False          | ()            | False        |
|  457 | requirement\_seq                                      | True       | True           | ()            | True         |
|  458 | constraint\_conjunction                               | True       | True           | ()            | True         |
|  459 | constraint\_disjunction                               | True       | True           | ()            | True         |
|  460 | \_requirement\_clause\_constraint                     | False      | False          | ()            | False        |
|  461 | requires\_clause                                      | True       | True           | ()            | True         |
|  462 | parameter\_list                                       | True       | True           | ()            | True         |
|  463 | requires\_expression                                  | True       | True           | ()            | True         |
|  464 | lambda\_expression                                    | True       | True           | ()            | True         |
|  465 | lambda\_capture\_specifier                            | True       | True           | ()            | True         |
|  466 | lambda\_default\_capture                              | True       | True           | ()            | True         |
|  467 | \_lambda\_capture\_identifier                         | False      | False          | ()            | False        |
|  468 | lambda\_capture\_initializer                          | True       | True           | ()            | True         |
|  469 | \_lambda\_capture                                     | False      | False          | ()            | False        |
|  470 | \_fold\_operator                                      | False      | False          | ()            | False        |
|  471 | \_binary\_fold\_operator                              | False      | False          | ()            | False        |
|  472 | \_unary\_left\_fold                                   | False      | False          | ()            | False        |
|  473 | \_unary\_right\_fold                                  | False      | False          | ()            | False        |
|  474 | \_binary\_fold                                        | False      | False          | ()            | False        |
|  475 | fold\_expression                                      | True       | True           | ()            | True         |
|  476 | parameter\_pack\_expansion                            | True       | True           | ()            | True         |
|  477 | parameter\_pack\_expansion                            | True       | True           | ()            | True         |
|  478 | parameter\_pack\_expansion                            | True       | True           | ()            | True         |
|  479 | destructor\_name                                      | True       | True           | ()            | True         |
|  480 | dependent\_name                                       | True       | True           | ()            | True         |
|  481 | dependent\_name                                       | True       | True           | ()            | True         |
|  482 | dependent\_name                                       | True       | True           | ()            | True         |
|  483 | \_scope\_resolution                                   | False      | False          | ()            | False        |
|  484 | qualified\_identifier                                 | True       | True           | ()            | True         |
|  485 | qualified\_identifier                                 | True       | True           | ()            | True         |
|  486 | qualified\_identifier                                 | True       | True           | ()            | True         |
|  487 | qualified\_identifier                                 | True       | True           | ()            | True         |
|  488 | assignment\_expression                                | True       | True           | ()            | True         |
|  489 | operator\_name                                        | True       | True           | ()            | True         |
|  490 | user\_defined\_literal                                | True       | True           | ()            | True         |
|  491 | translation\_unit\_repeat1                            | False      | False          | ()            | False        |
|  492 | preproc\_params\_repeat1                              | False      | False          | ()            | False        |
|  493 | preproc\_if\_repeat1                                  | False      | False          | ()            | False        |
|  494 | preproc\_if\_in\_field\_declaration\_list\_repeat1    | False      | False          | ()            | False        |
|  495 | preproc\_if\_in\_enumerator\_list\_repeat1            | False      | False          | ()            | False        |
|  496 | preproc\_if\_in\_enumerator\_list\_no\_comma\_repeat1 | False      | False          | ()            | False        |
|  497 | preproc\_argument\_list\_repeat1                      | False      | False          | ()            | False        |
|  498 | declaration\_repeat1                                  | False      | False          | ()            | False        |
|  499 | type\_definition\_repeat1                             | False      | False          | ()            | False        |
|  500 | \_type\_definition\_type\_repeat1                     | False      | False          | ()            | False        |
|  501 | \_type\_definition\_declarators\_repeat1              | False      | False          | ()            | False        |
|  502 | \_declaration\_specifiers\_repeat1                    | False      | False          | ()            | False        |
|  503 | attribute\_declaration\_repeat1                       | False      | False          | ()            | False        |
|  504 | attributed\_declarator\_repeat1                       | False      | False          | ()            | False        |
|  505 | pointer\_declarator\_repeat1                          | False      | False          | ()            | False        |
|  506 | array\_declarator\_repeat1                            | False      | False          | ()            | False        |
|  507 | sized\_type\_specifier\_repeat1                       | False      | False          | ()            | False        |
|  508 | enumerator\_list\_repeat1                             | False      | False          | ()            | False        |
|  509 | field\_declaration\_repeat1                           | False      | False          | ()            | False        |
|  510 | parameter\_list\_repeat1                              | False      | False          | ()            | False        |
|  511 | case\_statement\_repeat1                              | False      | False          | ()            | False        |
|  512 | generic\_expression\_repeat1                          | False      | False          | ()            | False        |
|  513 | gnu\_asm\_expression\_repeat1                         | False      | False          | ()            | False        |
|  514 | gnu\_asm\_output\_operand\_list\_repeat1              | False      | False          | ()            | False        |
|  515 | gnu\_asm\_input\_operand\_list\_repeat1               | False      | False          | ()            | False        |
|  516 | gnu\_asm\_clobber\_list\_repeat1                      | False      | False          | ()            | False        |
|  517 | gnu\_asm\_goto\_list\_repeat1                         | False      | False          | ()            | False        |
|  518 | argument\_list\_repeat1                               | False      | False          | ()            | False        |
|  519 | initializer\_list\_repeat1                            | False      | False          | ()            | False        |
|  520 | initializer\_pair\_repeat1                            | False      | False          | ()            | False        |
|  521 | char\_literal\_repeat1                                | False      | False          | ()            | False        |
|  522 | concatenated\_string\_repeat1                         | False      | False          | ()            | False        |
|  523 | string\_literal\_repeat1                              | False      | False          | ()            | False        |
|  524 | \_class\_declaration\_repeat1                         | False      | False          | ()            | False        |
|  525 | base\_class\_clause\_repeat1                          | False      | False          | ()            | False        |
|  526 | template\_parameter\_list\_repeat1                    | False      | False          | ()            | False        |
|  527 | field\_initializer\_list\_repeat1                     | False      | False          | ()            | False        |
|  528 | operator\_cast\_definition\_repeat1                   | False      | False          | ()            | False        |
|  529 | constructor\_try\_statement\_repeat1                  | False      | False          | ()            | False        |
|  530 | structured\_binding\_declarator\_repeat1              | False      | False          | ()            | False        |
|  531 | \_function\_postfix\_repeat1                          | False      | False          | ()            | False        |
|  532 | throw\_specifier\_repeat1                             | False      | False          | ()            | False        |
|  533 | template\_argument\_list\_repeat1                     | False      | False          | ()            | False        |
|  534 | subscript\_argument\_list\_repeat1                    | False      | False          | ()            | False        |
|  535 | requirement\_seq\_repeat1                             | False      | False          | ()            | False        |
|  536 | requires\_parameter\_list\_repeat1                    | False      | False          | ()            | False        |
|  537 | lambda\_capture\_specifier\_repeat1                   | False      | False          | ()            | False        |
|  538 | field\_identifier                                     | True       | True           | ()            | True         |
|  539 | namespace\_identifier                                 | True       | True           | ()            | True         |
|  540 | simple\_requirement                                   | True       | True           | ()            | True         |
|  541 | statement\_identifier                                 | True       | True           | ()            | True         |
|  542 | type\_identifier                                      | True       | True           | ()            | True         |

## Fields

|   id | name                 |
|------|----------------------|
|    0 | `None`               |
|    1 | alternative          |
|    2 | argument             |
|    3 | arguments            |
|    4 | assembly\_code       |
|    5 | base                 |
|    6 | body                 |
|    7 | captures             |
|    8 | clobbers             |
|    9 | condition            |
|   10 | consequence          |
|   11 | constraint           |
|   12 | declarator           |
|   13 | default\_type        |
|   14 | default\_value       |
|   15 | delimiter            |
|   16 | designator           |
|   17 | directive            |
|   18 | end                  |
|   19 | field                |
|   20 | filter               |
|   21 | function             |
|   22 | goto\_labels         |
|   23 | indices              |
|   24 | initializer          |
|   25 | input\_operands      |
|   26 | label                |
|   27 | left                 |
|   28 | length               |
|   29 | member               |
|   30 | message              |
|   31 | name                 |
|   32 | operand              |
|   33 | operator             |
|   34 | output\_operands     |
|   35 | parameters           |
|   36 | path                 |
|   37 | pattern              |
|   38 | placement            |
|   39 | prefix               |
|   40 | register             |
|   41 | requirements         |
|   42 | right                |
|   43 | scope                |
|   44 | size                 |
|   45 | start                |
|   46 | symbol               |
|   47 | template\_parameters |
|   48 | type                 |
|   49 | update               |


# CSS

- Language: css
- ABI version: 15
- File name extensions: ['.css']
- File name patterns: []
- Node kinds count: 151
    - Anonymous node count: 69
    - Visible node count: 126
    - Supertype node count: 126
- Field count: 0

## Node kinds

|   id | name                                  | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|---------------------------------------|------------|----------------|---------------|--------------|
|    0 | end                                   | False      | False          | ()            | False        |
|    1 | @import                               | False      | True           | ()            | True         |
|    2 | ,                                     | False      | True           | ()            | True         |
|    3 | ;                                     | False      | True           | ()            | True         |
|    4 | @media                                | False      | True           | ()            | True         |
|    5 | @charset                              | False      | True           | ()            | True         |
|    6 | @namespace                            | False      | True           | ()            | True         |
|    7 | @keyframes                            | False      | True           | ()            | True         |
|    8 | at\_keyword                           | True       | True           | ()            | True         |
|    9 | {                                     | False      | True           | ()            | True         |
|   10 | }                                     | False      | True           | ()            | True         |
|   11 | from                                  | True       | True           | ()            | True         |
|   12 | to                                    | False      | True           | ()            | True         |
|   13 | @supports                             | False      | True           | ()            | True         |
|   14 | @scope                                | False      | True           | ()            | True         |
|   15 | (                                     | False      | True           | ()            | True         |
|   16 | )                                     | False      | True           | ()            | True         |
|   17 | nesting\_selector                     | True       | True           | ()            | True         |
|   18 | \*                                    | False      | True           | ()            | True         |
|   19 | .                                     | False      | True           | ()            | True         |
|   20 | class\_name                           | True       | True           | ()            | True         |
|   21 | not                                   | False      | True           | ()            | True         |
|   22 | class\_name                           | True       | True           | ()            | True         |
|   23 | class\_name                           | True       | True           | ()            | True         |
|   24 | class\_name                           | True       | True           | ()            | True         |
|   25 | class\_name                           | True       | True           | ()            | True         |
|   26 | class\_name                           | True       | True           | ()            | True         |
|   27 | class\_name                           | True       | True           | ()            | True         |
|   28 | ::                                    | False      | True           | ()            | True         |
|   29 | #                                     | False      | True           | ()            | True         |
|   30 | [                                     | False      | True           | ()            | True         |
|   31 | =                                     | False      | True           | ()            | True         |
|   32 | ~=                                    | False      | True           | ()            | True         |
|   33 | ^=                                    | False      | True           | ()            | True         |
|   34 | &#124;=                               | False      | True           | ()            | True         |
|   35 | \*=                                   | False      | True           | ()            | True         |
|   36 | $=                                    | False      | True           | ()            | True         |
|   37 | ]                                     | False      | True           | ()            | True         |
|   38 | &gt;                                  | False      | True           | ()            | True         |
|   39 | ~                                     | False      | True           | ()            | True         |
|   40 | +                                     | False      | True           | ()            | True         |
|   41 | &#124;                                | False      | True           | ()            | True         |
|   42 | (                                     | False      | True           | ()            | True         |
|   43 | plain\_value                          | True       | True           | ()            | True         |
|   44 | plain\_value                          | True       | True           | ()            | True         |
|   45 | of                                    | False      | True           | ()            | True         |
|   46 | plain\_value                          | True       | True           | ()            | True         |
|   47 | :                                     | False      | True           | ()            | True         |
|   48 | important                             | True       | True           | ()            | True         |
|   49 | and                                   | False      | True           | ()            | True         |
|   50 | or                                    | False      | True           | ()            | True         |
|   51 | only                                  | False      | True           | ()            | True         |
|   52 | selector                              | False      | True           | ()            | True         |
|   53 | color\_value\_token1                  | False      | False          | ()            | False        |
|   54 | '                                     | False      | True           | ()            | True         |
|   55 | string\_content                       | True       | True           | ()            | True         |
|   56 | "                                     | False      | True           | ()            | True         |
|   57 | string\_content                       | True       | True           | ()            | True         |
|   58 | escape\_sequence                      | True       | True           | ()            | True         |
|   59 | integer\_value\_token1                | False      | False          | ()            | False        |
|   60 | float\_value\_token1                  | False      | False          | ()            | False        |
|   61 | unit                                  | True       | True           | ()            | True         |
|   62 | [                                     | False      | True           | ()            | True         |
|   63 | -                                     | False      | True           | ()            | True         |
|   64 | /                                     | False      | True           | ()            | True         |
|   65 | identifier                            | True       | True           | ()            | True         |
|   66 | identifier                            | True       | True           | ()            | True         |
|   67 | at\_keyword                           | True       | True           | ()            | True         |
|   68 | js\_comment                           | True       | True           | ()            | True         |
|   69 | comment                               | True       | True           | ()            | True         |
|   70 | plain\_value                          | True       | True           | ()            | True         |
|   71 | important\_value                      | True       | True           | ()            | True         |
|   72 | \_descendant\_operator                | False      | False          | ()            | False        |
|   73 | :                                     | False      | True           | ()            | True         |
|   74 | \_\_error\_recovery                   | False      | False          | ()            | False        |
|   75 | stylesheet                            | True       | True           | ()            | True         |
|   76 | import\_statement                     | True       | True           | ()            | True         |
|   77 | media\_statement                      | True       | True           | ()            | True         |
|   78 | charset\_statement                    | True       | True           | ()            | True         |
|   79 | namespace\_statement                  | True       | True           | ()            | True         |
|   80 | keyframes\_statement                  | True       | True           | ()            | True         |
|   81 | keyframe\_block\_list                 | True       | True           | ()            | True         |
|   82 | keyframe\_block                       | True       | True           | ()            | True         |
|   83 | to                                    | True       | True           | ()            | True         |
|   84 | supports\_statement                   | True       | True           | ()            | True         |
|   85 | scope\_statement                      | True       | True           | ()            | True         |
|   86 | postcss\_statement                    | True       | True           | ()            | True         |
|   87 | at\_rule                              | True       | True           | ()            | True         |
|   88 | rule\_set                             | True       | True           | ()            | True         |
|   89 | selectors                             | True       | True           | ()            | True         |
|   90 | block                                 | True       | True           | ()            | True         |
|   91 | \_selector                            | False      | False          | ()            | False        |
|   92 | universal\_selector                   | True       | True           | ()            | True         |
|   93 | class\_selector                       | True       | True           | ()            | True         |
|   94 | pseudo\_class\_selector               | True       | True           | ()            | True         |
|   95 | \_nth\_child\_pseudo\_class\_selector | False      | False          | ()            | False        |
|   96 | pseudo\_element\_selector             | True       | True           | ()            | True         |
|   97 | id\_selector                          | True       | True           | ()            | True         |
|   98 | attribute\_selector                   | True       | True           | ()            | True         |
|   99 | child\_selector                       | True       | True           | ()            | True         |
|  100 | descendant\_selector                  | True       | True           | ()            | True         |
|  101 | sibling\_selector                     | True       | True           | ()            | True         |
|  102 | adjacent\_sibling\_selector           | True       | True           | ()            | True         |
|  103 | namespace\_selector                   | True       | True           | ()            | True         |
|  104 | arguments                             | True       | True           | ()            | True         |
|  105 | arguments                             | True       | True           | ()            | True         |
|  106 | arguments                             | True       | True           | ()            | True         |
|  107 | arguments                             | True       | True           | ()            | True         |
|  108 | declaration                           | True       | True           | ()            | True         |
|  109 | declaration                           | True       | True           | ()            | True         |
|  110 | \_query                               | False      | False          | ()            | False        |
|  111 | feature\_query                        | True       | True           | ()            | True         |
|  112 | parenthesized\_query                  | True       | True           | ()            | True         |
|  113 | binary\_query                         | True       | True           | ()            | True         |
|  114 | unary\_query                          | True       | True           | ()            | True         |
|  115 | selector\_query                       | True       | True           | ()            | True         |
|  116 | \_value                               | False      | False          | ()            | False        |
|  117 | parenthesized\_value                  | True       | True           | ()            | True         |
|  118 | color\_value                          | True       | True           | ()            | True         |
|  119 | string\_value                         | True       | True           | ()            | True         |
|  120 | integer\_value                        | True       | True           | ()            | True         |
|  121 | float\_value                          | True       | True           | ()            | True         |
|  122 | grid\_value                           | True       | True           | ()            | True         |
|  123 | call\_expression                      | True       | True           | ()            | True         |
|  124 | binary\_expression                    | True       | True           | ()            | True         |
|  125 | arguments                             | True       | True           | ()            | True         |
|  126 | class\_name                           | True       | True           | ()            | True         |
|  127 | stylesheet\_repeat1                   | False      | False          | ()            | False        |
|  128 | import\_statement\_repeat1            | False      | False          | ()            | False        |
|  129 | keyframe\_block\_list\_repeat1        | False      | False          | ()            | False        |
|  130 | keyframe\_block\_repeat1              | False      | False          | ()            | False        |
|  131 | postcss\_statement\_repeat1           | False      | False          | ()            | False        |
|  132 | selectors\_repeat1                    | False      | False          | ()            | False        |
|  133 | block\_repeat1                        | False      | False          | ()            | False        |
|  134 | pseudo\_class\_arguments\_repeat1     | False      | False          | ()            | False        |
|  135 | pseudo\_class\_arguments\_repeat2     | False      | False          | ()            | False        |
|  136 | declaration\_repeat1                  | False      | False          | ()            | False        |
|  137 | string\_value\_repeat1                | False      | False          | ()            | False        |
|  138 | string\_value\_repeat2                | False      | False          | ()            | False        |
|  139 | grid\_value\_repeat1                  | False      | False          | ()            | False        |
|  140 | arguments\_repeat1                    | False      | False          | ()            | False        |
|  141 | class\_name\_repeat1                  | False      | False          | ()            | False        |
|  142 | attribute\_name                       | True       | True           | ()            | True         |
|  143 | feature\_name                         | True       | True           | ()            | True         |
|  144 | function\_name                        | True       | True           | ()            | True         |
|  145 | id\_name                              | True       | True           | ()            | True         |
|  146 | keyframes\_name                       | True       | True           | ()            | True         |
|  147 | keyword\_query                        | True       | True           | ()            | True         |
|  148 | namespace\_name                       | True       | True           | ()            | True         |
|  149 | property\_name                        | True       | True           | ()            | True         |
|  150 | tag\_name                             | True       | True           | ()            | True         |

## Fields




# GO

- Language: go
- ABI version: 15
- File name extensions: ['.go']
- File name patterns: []
- Node kinds count: 219
    - Anonymous node count: 108
    - Visible node count: 188
    - Supertype node count: 192
- Field count: 35

## Node kinds

|   id | name                                   | is_named   | is_supertype   | subtype_ids                                                                                                       | is_visible   |
|------|----------------------------------------|------------|----------------|-------------------------------------------------------------------------------------------------------------------|--------------|
|    0 | end                                    | False      | False          | ()                                                                                                                | False        |
|    1 | identifier                             | True       | True           | ()                                                                                                                | True         |
|    2 | source\_file\_token1                   | False      | False          | ()                                                                                                                | False        |
|    3 | ;                                      | False      | True           | ()                                                                                                                | True         |
|    4 |                                        | False      | True           | ()                                                                                                                | True         |
|    5 | package                                | False      | True           | ()                                                                                                                | True         |
|    6 | import                                 | False      | True           | ()                                                                                                                | True         |
|    7 | .                                      | False      | True           | ()                                                                                                                | True         |
|    8 | blank\_identifier                      | True       | True           | ()                                                                                                                | True         |
|    9 | (                                      | False      | True           | ()                                                                                                                | True         |
|   10 | )                                      | False      | True           | ()                                                                                                                | True         |
|   11 | const                                  | False      | True           | ()                                                                                                                | True         |
|   12 | ,                                      | False      | True           | ()                                                                                                                | True         |
|   13 | =                                      | False      | True           | ()                                                                                                                | True         |
|   14 | var                                    | False      | True           | ()                                                                                                                | True         |
|   15 | func                                   | False      | True           | ()                                                                                                                | True         |
|   16 | [                                      | False      | True           | ()                                                                                                                | True         |
|   17 | ]                                      | False      | True           | ()                                                                                                                | True         |
|   18 | ...                                    | False      | True           | ()                                                                                                                | True         |
|   19 | type                                   | False      | True           | ()                                                                                                                | True         |
|   20 | \*                                     | False      | True           | ()                                                                                                                | True         |
|   21 | struct                                 | False      | True           | ()                                                                                                                | True         |
|   22 | ~                                      | False      | True           | ()                                                                                                                | True         |
|   23 | {                                      | False      | True           | ()                                                                                                                | True         |
|   24 | }                                      | False      | True           | ()                                                                                                                | True         |
|   25 | interface                              | False      | True           | ()                                                                                                                | True         |
|   26 | &#124;                                 | False      | True           | ()                                                                                                                | True         |
|   27 | map                                    | False      | True           | ()                                                                                                                | True         |
|   28 | chan                                   | False      | True           | ()                                                                                                                | True         |
|   29 | &lt;-                                  | False      | True           | ()                                                                                                                | True         |
|   30 | :=                                     | False      | True           | ()                                                                                                                | True         |
|   31 | ++                                     | False      | True           | ()                                                                                                                | True         |
|   32 | --                                     | False      | True           | ()                                                                                                                | True         |
|   33 | \*=                                    | False      | True           | ()                                                                                                                | True         |
|   34 | /=                                     | False      | True           | ()                                                                                                                | True         |
|   35 | %=                                     | False      | True           | ()                                                                                                                | True         |
|   36 | &lt;&lt;=                              | False      | True           | ()                                                                                                                | True         |
|   37 | &gt;&gt;=                              | False      | True           | ()                                                                                                                | True         |
|   38 | &amp;=                                 | False      | True           | ()                                                                                                                | True         |
|   39 | &amp;^=                                | False      | True           | ()                                                                                                                | True         |
|   40 | +=                                     | False      | True           | ()                                                                                                                | True         |
|   41 | -=                                     | False      | True           | ()                                                                                                                | True         |
|   42 | &#124;=                                | False      | True           | ()                                                                                                                | True         |
|   43 | ^=                                     | False      | True           | ()                                                                                                                | True         |
|   44 | :                                      | False      | True           | ()                                                                                                                | True         |
|   45 | fallthrough                            | False      | True           | ()                                                                                                                | True         |
|   46 | break                                  | False      | True           | ()                                                                                                                | True         |
|   47 | continue                               | False      | True           | ()                                                                                                                | True         |
|   48 | goto                                   | False      | True           | ()                                                                                                                | True         |
|   49 | return                                 | False      | True           | ()                                                                                                                | True         |
|   50 | go                                     | False      | True           | ()                                                                                                                | True         |
|   51 | defer                                  | False      | True           | ()                                                                                                                | True         |
|   52 | if                                     | False      | True           | ()                                                                                                                | True         |
|   53 | else                                   | False      | True           | ()                                                                                                                | True         |
|   54 | for                                    | False      | True           | ()                                                                                                                | True         |
|   55 | range                                  | False      | True           | ()                                                                                                                | True         |
|   56 | switch                                 | False      | True           | ()                                                                                                                | True         |
|   57 | case                                   | False      | True           | ()                                                                                                                | True         |
|   58 | default                                | False      | True           | ()                                                                                                                | True         |
|   59 | select                                 | False      | True           | ()                                                                                                                | True         |
|   60 | identifier                             | True       | True           | ()                                                                                                                | True         |
|   61 | identifier                             | True       | True           | ()                                                                                                                | True         |
|   62 | +                                      | False      | True           | ()                                                                                                                | True         |
|   63 | -                                      | False      | True           | ()                                                                                                                | True         |
|   64 | !                                      | False      | True           | ()                                                                                                                | True         |
|   65 | ^                                      | False      | True           | ()                                                                                                                | True         |
|   66 | &amp;                                  | False      | True           | ()                                                                                                                | True         |
|   67 | /                                      | False      | True           | ()                                                                                                                | True         |
|   68 | %                                      | False      | True           | ()                                                                                                                | True         |
|   69 | &lt;&lt;                               | False      | True           | ()                                                                                                                | True         |
|   70 | &gt;&gt;                               | False      | True           | ()                                                                                                                | True         |
|   71 | &amp;^                                 | False      | True           | ()                                                                                                                | True         |
|   72 | ==                                     | False      | True           | ()                                                                                                                | True         |
|   73 | !=                                     | False      | True           | ()                                                                                                                | True         |
|   74 | &lt;                                   | False      | True           | ()                                                                                                                | True         |
|   75 | &lt;=                                  | False      | True           | ()                                                                                                                | True         |
|   76 | &gt;                                   | False      | True           | ()                                                                                                                | True         |
|   77 | &gt;=                                  | False      | True           | ()                                                                                                                | True         |
|   78 | &amp;&amp;                             | False      | True           | ()                                                                                                                | True         |
|   79 | &#124;&#124;                           | False      | True           | ()                                                                                                                | True         |
|   80 | \`                                     | False      | True           | ()                                                                                                                | True         |
|   81 | raw\_string\_literal\_content          | True       | True           | ()                                                                                                                | True         |
|   82 | "                                      | False      | True           | ()                                                                                                                | True         |
|   83 | interpreted\_string\_literal\_content  | True       | True           | ()                                                                                                                | True         |
|   84 | "                                      | False      | True           | ()                                                                                                                | True         |
|   85 | escape\_sequence                       | True       | True           | ()                                                                                                                | True         |
|   86 | int\_literal                           | True       | True           | ()                                                                                                                | True         |
|   87 | float\_literal                         | True       | True           | ()                                                                                                                | True         |
|   88 | imaginary\_literal                     | True       | True           | ()                                                                                                                | True         |
|   89 | rune\_literal                          | True       | True           | ()                                                                                                                | True         |
|   90 | nil                                    | True       | True           | ()                                                                                                                | True         |
|   91 | true                                   | True       | True           | ()                                                                                                                | True         |
|   92 | false                                  | True       | True           | ()                                                                                                                | True         |
|   93 | iota                                   | True       | True           | ()                                                                                                                | True         |
|   94 | comment                                | True       | True           | ()                                                                                                                | True         |
|   95 | source\_file                           | True       | True           | ()                                                                                                                | True         |
|   96 | package\_clause                        | True       | True           | ()                                                                                                                | True         |
|   97 | import\_declaration                    | True       | True           | ()                                                                                                                | True         |
|   98 | import\_spec                           | True       | True           | ()                                                                                                                | True         |
|   99 | dot                                    | True       | True           | ()                                                                                                                | True         |
|  100 | import\_spec\_list                     | True       | True           | ()                                                                                                                | True         |
|  101 | \_declaration                          | False      | False          | ()                                                                                                                | False        |
|  102 | const\_declaration                     | True       | True           | ()                                                                                                                | True         |
|  103 | const\_spec                            | True       | True           | ()                                                                                                                | True         |
|  104 | var\_declaration                       | True       | True           | ()                                                                                                                | True         |
|  105 | var\_spec                              | True       | True           | ()                                                                                                                | True         |
|  106 | var\_spec\_list                        | True       | True           | ()                                                                                                                | True         |
|  107 | function\_declaration                  | True       | True           | ()                                                                                                                | True         |
|  108 | method\_declaration                    | True       | True           | ()                                                                                                                | True         |
|  109 | type\_parameter\_list                  | True       | True           | ()                                                                                                                | True         |
|  110 | type\_parameter\_declaration           | True       | True           | ()                                                                                                                | True         |
|  111 | parameter\_list                        | True       | True           | ()                                                                                                                | True         |
|  112 | parameter\_declaration                 | True       | True           | ()                                                                                                                | True         |
|  113 | variadic\_parameter\_declaration       | True       | True           | ()                                                                                                                | True         |
|  114 | type\_alias                            | True       | True           | ()                                                                                                                | True         |
|  115 | type\_declaration                      | True       | True           | ()                                                                                                                | True         |
|  116 | type\_spec                             | True       | True           | ()                                                                                                                | True         |
|  117 | expression\_list                       | True       | True           | ()                                                                                                                | True         |
|  118 | parenthesized\_type                    | True       | True           | ()                                                                                                                | True         |
|  119 | \_simple\_type                         | False      | True           | (218, 123, 134, 135, 120, 130, 133, 127, 122, 188, 125, 126)                                                      | False        |
|  120 | generic\_type                          | True       | True           | ()                                                                                                                | True         |
|  121 | type\_arguments                        | True       | True           | ()                                                                                                                | True         |
|  122 | pointer\_type                          | True       | True           | ()                                                                                                                | True         |
|  123 | array\_type                            | True       | True           | ()                                                                                                                | True         |
|  124 | implicit\_length\_array\_type          | True       | True           | ()                                                                                                                | True         |
|  125 | slice\_type                            | True       | True           | ()                                                                                                                | True         |
|  126 | struct\_type                           | True       | True           | ()                                                                                                                | True         |
|  127 | negated\_type                          | True       | True           | ()                                                                                                                | True         |
|  128 | field\_declaration\_list               | True       | True           | ()                                                                                                                | True         |
|  129 | field\_declaration                     | True       | True           | ()                                                                                                                | True         |
|  130 | interface\_type                        | True       | True           | ()                                                                                                                | True         |
|  131 | method\_elem                           | True       | True           | ()                                                                                                                | True         |
|  132 | type\_elem                             | True       | True           | ()                                                                                                                | True         |
|  133 | map\_type                              | True       | True           | ()                                                                                                                | True         |
|  134 | channel\_type                          | True       | True           | ()                                                                                                                | True         |
|  135 | function\_type                         | True       | True           | ()                                                                                                                | True         |
|  136 | block                                  | True       | True           | ()                                                                                                                | True         |
|  137 | statement\_list                        | True       | True           | ()                                                                                                                | True         |
|  138 | \_statement                            | False      | True           | (140, 136, 151, 102, 152, 156, 139, 161, 150, 158, 155, 153, 157, 148, 154, 167, 115, 164, 104)                   | False        |
|  139 | empty\_statement                       | True       | True           | ()                                                                                                                | True         |
|  140 | \_simple\_statement                    | False      | True           | (146, 145, 141, 144, 142, 147)                                                                                    | False        |
|  141 | expression\_statement                  | True       | True           | ()                                                                                                                | True         |
|  142 | send\_statement                        | True       | True           | ()                                                                                                                | True         |
|  143 | receive\_statement                     | True       | True           | ()                                                                                                                | True         |
|  144 | inc\_statement                         | True       | True           | ()                                                                                                                | True         |
|  145 | dec\_statement                         | True       | True           | ()                                                                                                                | True         |
|  146 | assignment\_statement                  | True       | True           | ()                                                                                                                | True         |
|  147 | short\_var\_declaration                | True       | True           | ()                                                                                                                | True         |
|  148 | labeled\_statement                     | True       | True           | ()                                                                                                                | True         |
|  149 | labeled\_statement                     | True       | True           | ()                                                                                                                | True         |
|  150 | fallthrough\_statement                 | True       | True           | ()                                                                                                                | True         |
|  151 | break\_statement                       | True       | True           | ()                                                                                                                | True         |
|  152 | continue\_statement                    | True       | True           | ()                                                                                                                | True         |
|  153 | goto\_statement                        | True       | True           | ()                                                                                                                | True         |
|  154 | return\_statement                      | True       | True           | ()                                                                                                                | True         |
|  155 | go\_statement                          | True       | True           | ()                                                                                                                | True         |
|  156 | defer\_statement                       | True       | True           | ()                                                                                                                | True         |
|  157 | if\_statement                          | True       | True           | ()                                                                                                                | True         |
|  158 | for\_statement                         | True       | True           | ()                                                                                                                | True         |
|  159 | for\_clause                            | True       | True           | ()                                                                                                                | True         |
|  160 | range\_clause                          | True       | True           | ()                                                                                                                | True         |
|  161 | expression\_switch\_statement          | True       | True           | ()                                                                                                                | True         |
|  162 | expression\_case                       | True       | True           | ()                                                                                                                | True         |
|  163 | default\_case                          | True       | True           | ()                                                                                                                | True         |
|  164 | type\_switch\_statement                | True       | True           | ()                                                                                                                | True         |
|  165 | \_type\_switch\_header                 | False      | False          | ()                                                                                                                | False        |
|  166 | type\_case                             | True       | True           | ()                                                                                                                | True         |
|  167 | select\_statement                      | True       | True           | ()                                                                                                                | True         |
|  168 | communication\_case                    | True       | True           | ()                                                                                                                | True         |
|  169 | \_expression                           | False      | True           | (61, 60, 187, 171, 181, 92, 87, 185, 1, 88, 176, 86, 190, 93, 90, 170, 189, 89, 175, 177, 91, 178, 179, 180, 186) | False        |
|  170 | parenthesized\_expression              | True       | True           | ()                                                                                                                | True         |
|  171 | call\_expression                       | True       | True           | ()                                                                                                                | True         |
|  172 | variadic\_argument                     | True       | True           | ()                                                                                                                | True         |
|  173 | argument\_list                         | True       | True           | ()                                                                                                                | True         |
|  174 | argument\_list                         | True       | True           | ()                                                                                                                | True         |
|  175 | selector\_expression                   | True       | True           | ()                                                                                                                | True         |
|  176 | index\_expression                      | True       | True           | ()                                                                                                                | True         |
|  177 | slice\_expression                      | True       | True           | ()                                                                                                                | True         |
|  178 | type\_assertion\_expression            | True       | True           | ()                                                                                                                | True         |
|  179 | type\_conversion\_expression           | True       | True           | ()                                                                                                                | True         |
|  180 | type\_instantiation\_expression        | True       | True           | ()                                                                                                                | True         |
|  181 | composite\_literal                     | True       | True           | ()                                                                                                                | True         |
|  182 | literal\_value                         | True       | True           | ()                                                                                                                | True         |
|  183 | literal\_element                       | True       | True           | ()                                                                                                                | True         |
|  184 | keyed\_element                         | True       | True           | ()                                                                                                                | True         |
|  185 | func\_literal                          | True       | True           | ()                                                                                                                | True         |
|  186 | unary\_expression                      | True       | True           | ()                                                                                                                | True         |
|  187 | binary\_expression                     | True       | True           | ()                                                                                                                | True         |
|  188 | qualified\_type                        | True       | True           | ()                                                                                                                | True         |
|  189 | raw\_string\_literal                   | True       | True           | ()                                                                                                                | True         |
|  190 | interpreted\_string\_literal           | True       | True           | ()                                                                                                                | True         |
|  191 | source\_file\_repeat1                  | False      | False          | ()                                                                                                                | False        |
|  192 | import\_spec\_list\_repeat1            | False      | False          | ()                                                                                                                | False        |
|  193 | const\_declaration\_repeat1            | False      | False          | ()                                                                                                                | False        |
|  194 | const\_spec\_repeat1                   | False      | False          | ()                                                                                                                | False        |
|  195 | var\_spec\_repeat1                     | False      | False          | ()                                                                                                                | False        |
|  196 | var\_spec\_list\_repeat1               | False      | False          | ()                                                                                                                | False        |
|  197 | type\_parameter\_list\_repeat1         | False      | False          | ()                                                                                                                | False        |
|  198 | parameter\_list\_repeat1               | False      | False          | ()                                                                                                                | False        |
|  199 | type\_declaration\_repeat1             | False      | False          | ()                                                                                                                | False        |
|  200 | expression\_list\_repeat1              | False      | False          | ()                                                                                                                | False        |
|  201 | type\_arguments\_repeat1               | False      | False          | ()                                                                                                                | False        |
|  202 | field\_declaration\_list\_repeat1      | False      | False          | ()                                                                                                                | False        |
|  203 | field\_declaration\_repeat1            | False      | False          | ()                                                                                                                | False        |
|  204 | interface\_type\_repeat1               | False      | False          | ()                                                                                                                | False        |
|  205 | type\_elem\_repeat1                    | False      | False          | ()                                                                                                                | False        |
|  206 | statement\_list\_repeat1               | False      | False          | ()                                                                                                                | False        |
|  207 | expression\_switch\_statement\_repeat1 | False      | False          | ()                                                                                                                | False        |
|  208 | type\_switch\_statement\_repeat1       | False      | False          | ()                                                                                                                | False        |
|  209 | type\_case\_repeat1                    | False      | False          | ()                                                                                                                | False        |
|  210 | select\_statement\_repeat1             | False      | False          | ()                                                                                                                | False        |
|  211 | argument\_list\_repeat1                | False      | False          | ()                                                                                                                | False        |
|  212 | literal\_value\_repeat1                | False      | False          | ()                                                                                                                | False        |
|  213 | interpreted\_string\_literal\_repeat1  | False      | False          | ()                                                                                                                | False        |
|  214 | field\_identifier                      | True       | True           | ()                                                                                                                | True         |
|  215 | label\_name                            | True       | True           | ()                                                                                                                | True         |
|  216 | package\_identifier                    | True       | True           | ()                                                                                                                | True         |
|  217 | type\_constraint                       | True       | True           | ()                                                                                                                | True         |
|  218 | type\_identifier                       | True       | True           | ()                                                                                                                | True         |

## Fields

|   id | name             |
|------|------------------|
|    0 | `None`           |
|    1 | alias            |
|    2 | alternative      |
|    3 | arguments        |
|    4 | body             |
|    5 | capacity         |
|    6 | channel          |
|    7 | communication    |
|    8 | condition        |
|    9 | consequence      |
|   10 | element          |
|   11 | end              |
|   12 | field            |
|   13 | function         |
|   14 | index            |
|   15 | initializer      |
|   16 | key              |
|   17 | label            |
|   18 | left             |
|   19 | length           |
|   20 | name             |
|   21 | operand          |
|   22 | operator         |
|   23 | package          |
|   24 | parameters       |
|   25 | path             |
|   26 | receiver         |
|   27 | result           |
|   28 | right            |
|   29 | start            |
|   30 | tag              |
|   31 | type             |
|   32 | type\_arguments  |
|   33 | type\_parameters |
|   34 | update           |


# HTML

- Language: html
- ABI version: 14
- File name extensions: ['.html', '.htm']
- File name patterns: []
- Node kinds count: 41
    - Anonymous node count: 15
    - Visible node count: 35
    - Supertype node count: 35
- Field count: 0

## Node kinds

|   id | name                      | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|---------------------------|------------|----------------|---------------|--------------|
|    0 | end                       | False      | False          | ()            | False        |
|    1 | &lt;!                     | False      | True           | ()            | True         |
|    2 | doctype\_token1           | False      | False          | ()            | False        |
|    3 | &gt;                      | False      | True           | ()            | True         |
|    4 | doctype                   | False      | True           | ()            | True         |
|    5 | &lt;                      | False      | True           | ()            | True         |
|    6 | /&gt;                     | False      | True           | ()            | True         |
|    7 | &lt;/                     | False      | True           | ()            | True         |
|    8 | =                         | False      | True           | ()            | True         |
|    9 | attribute\_name           | True       | True           | ()            | True         |
|   10 | attribute\_value          | True       | True           | ()            | True         |
|   11 | entity                    | True       | True           | ()            | True         |
|   12 | '                         | False      | True           | ()            | True         |
|   13 | attribute\_value          | True       | True           | ()            | True         |
|   14 | "                         | False      | True           | ()            | True         |
|   15 | attribute\_value          | True       | True           | ()            | True         |
|   16 | text                      | True       | True           | ()            | True         |
|   17 | tag\_name                 | True       | True           | ()            | True         |
|   18 | tag\_name                 | True       | True           | ()            | True         |
|   19 | tag\_name                 | True       | True           | ()            | True         |
|   20 | tag\_name                 | True       | True           | ()            | True         |
|   21 | erroneous\_end\_tag\_name | True       | True           | ()            | True         |
|   22 | \_implicit\_end\_tag      | False      | False          | ()            | False        |
|   23 | raw\_text                 | True       | True           | ()            | True         |
|   24 | comment                   | True       | True           | ()            | True         |
|   25 | document                  | True       | True           | ()            | True         |
|   26 | doctype                   | True       | True           | ()            | True         |
|   27 | \_node                    | False      | False          | ()            | False        |
|   28 | element                   | True       | True           | ()            | True         |
|   29 | script\_element           | True       | True           | ()            | True         |
|   30 | style\_element            | True       | True           | ()            | True         |
|   31 | start\_tag                | True       | True           | ()            | True         |
|   32 | start\_tag                | True       | True           | ()            | True         |
|   33 | start\_tag                | True       | True           | ()            | True         |
|   34 | self\_closing\_tag        | True       | True           | ()            | True         |
|   35 | end\_tag                  | True       | True           | ()            | True         |
|   36 | erroneous\_end\_tag       | True       | True           | ()            | True         |
|   37 | attribute                 | True       | True           | ()            | True         |
|   38 | quoted\_attribute\_value  | True       | True           | ()            | True         |
|   39 | document\_repeat1         | False      | False          | ()            | False        |
|   40 | start\_tag\_repeat1       | False      | False          | ()            | False        |

## Fields




# JAVA

- Language: java
- ABI version: 14
- File name extensions: ['.java']
- File name patterns: []
- Node kinds count: 321
    - Anonymous node count: 179
    - Visible node count: 256
    - Supertype node count: 264
- Field count: 40

## Node kinds

|   id | name                                        | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|---------------------------------------------|------------|----------------|---------------|--------------|
|    0 | end                                         | False      | False          | ()            | False        |
|    1 | identifier                                  | True       | True           | ()            | True         |
|    2 | decimal\_integer\_literal                   | True       | True           | ()            | True         |
|    3 | hex\_integer\_literal                       | True       | True           | ()            | True         |
|    4 | octal\_integer\_literal                     | True       | True           | ()            | True         |
|    5 | binary\_integer\_literal                    | True       | True           | ()            | True         |
|    6 | decimal\_floating\_point\_literal           | True       | True           | ()            | True         |
|    7 | hex\_floating\_point\_literal               | True       | True           | ()            | True         |
|    8 | true                                        | True       | True           | ()            | True         |
|    9 | false                                       | True       | True           | ()            | True         |
|   10 | character\_literal                          | True       | True           | ()            | True         |
|   11 | "                                           | False      | True           | ()            | True         |
|   12 | """                                         | False      | True           | ()            | True         |
|   13 | string\_fragment                            | True       | True           | ()            | True         |
|   14 | \_multiline\_string\_fragment\_token1       | False      | False          | ()            | False        |
|   15 | \_multiline\_string\_fragment\_token2       | False      | False          | ()            | False        |
|   16 | \{                                          | False      | True           | ()            | True         |
|   17 | }                                           | False      | True           | ()            | True         |
|   18 | \_escape\_sequence\_token1                  | False      | False          | ()            | False        |
|   19 | escape\_sequence                            | True       | True           | ()            | True         |
|   20 | null\_literal                               | True       | True           | ()            | True         |
|   21 | (                                           | False      | True           | ()            | True         |
|   22 | )                                           | False      | True           | ()            | True         |
|   23 | &amp;                                       | False      | True           | ()            | True         |
|   24 | =                                           | False      | True           | ()            | True         |
|   25 | +=                                          | False      | True           | ()            | True         |
|   26 | -=                                          | False      | True           | ()            | True         |
|   27 | \*=                                         | False      | True           | ()            | True         |
|   28 | /=                                          | False      | True           | ()            | True         |
|   29 | &amp;=                                      | False      | True           | ()            | True         |
|   30 | &#124;=                                     | False      | True           | ()            | True         |
|   31 | ^=                                          | False      | True           | ()            | True         |
|   32 | %=                                          | False      | True           | ()            | True         |
|   33 | &lt;&lt;=                                   | False      | True           | ()            | True         |
|   34 | &gt;&gt;=                                   | False      | True           | ()            | True         |
|   35 | &gt;&gt;&gt;=                               | False      | True           | ()            | True         |
|   36 | &gt;                                        | False      | True           | ()            | True         |
|   37 | &lt;                                        | False      | True           | ()            | True         |
|   38 | &gt;=                                       | False      | True           | ()            | True         |
|   39 | &lt;=                                       | False      | True           | ()            | True         |
|   40 | ==                                          | False      | True           | ()            | True         |
|   41 | !=                                          | False      | True           | ()            | True         |
|   42 | &amp;&amp;                                  | False      | True           | ()            | True         |
|   43 | &#124;&#124;                                | False      | True           | ()            | True         |
|   44 | +                                           | False      | True           | ()            | True         |
|   45 | -                                           | False      | True           | ()            | True         |
|   46 | \*                                          | False      | True           | ()            | True         |
|   47 | /                                           | False      | True           | ()            | True         |
|   48 | &#124;                                      | False      | True           | ()            | True         |
|   49 | ^                                           | False      | True           | ()            | True         |
|   50 | %                                           | False      | True           | ()            | True         |
|   51 | &lt;&lt;                                    | False      | True           | ()            | True         |
|   52 | &gt;&gt;                                    | False      | True           | ()            | True         |
|   53 | &gt;&gt;&gt;                                | False      | True           | ()            | True         |
|   54 | instanceof                                  | False      | True           | ()            | True         |
|   55 | final                                       | False      | True           | ()            | True         |
|   56 | -&gt;                                       | False      | True           | ()            | True         |
|   57 | ,                                           | False      | True           | ()            | True         |
|   58 | ?                                           | False      | True           | ()            | True         |
|   59 | :                                           | False      | True           | ()            | True         |
|   60 | !                                           | False      | True           | ()            | True         |
|   61 | ~                                           | False      | True           | ()            | True         |
|   62 | ++                                          | False      | True           | ()            | True         |
|   63 | --                                          | False      | True           | ()            | True         |
|   64 | new                                         | False      | True           | ()            | True         |
|   65 | [                                           | False      | True           | ()            | True         |
|   66 | ]                                           | False      | True           | ()            | True         |
|   67 | .                                           | False      | True           | ()            | True         |
|   68 | class                                       | False      | True           | ()            | True         |
|   69 | ::                                          | False      | True           | ()            | True         |
|   70 | extends                                     | False      | True           | ()            | True         |
|   71 | switch                                      | False      | True           | ()            | True         |
|   72 | {                                           | False      | True           | ()            | True         |
|   73 | case                                        | False      | True           | ()            | True         |
|   74 | default                                     | False      | True           | ()            | True         |
|   75 | underscore\_pattern                         | True       | True           | ()            | True         |
|   76 | when                                        | False      | True           | ()            | True         |
|   77 | ;                                           | False      | True           | ()            | True         |
|   78 | assert                                      | False      | True           | ()            | True         |
|   79 | do                                          | False      | True           | ()            | True         |
|   80 | while                                       | False      | True           | ()            | True         |
|   81 | break                                       | False      | True           | ()            | True         |
|   82 | continue                                    | False      | True           | ()            | True         |
|   83 | return                                      | False      | True           | ()            | True         |
|   84 | yield                                       | False      | True           | ()            | True         |
|   85 | synchronized                                | False      | True           | ()            | True         |
|   86 | throw                                       | False      | True           | ()            | True         |
|   87 | try                                         | False      | True           | ()            | True         |
|   88 | catch                                       | False      | True           | ()            | True         |
|   89 | finally                                     | False      | True           | ()            | True         |
|   90 | if                                          | False      | True           | ()            | True         |
|   91 | else                                        | False      | True           | ()            | True         |
|   92 | for                                         | False      | True           | ()            | True         |
|   93 | @                                           | False      | True           | ()            | True         |
|   94 | open                                        | False      | True           | ()            | True         |
|   95 | module                                      | False      | True           | ()            | True         |
|   96 | requires                                    | False      | True           | ()            | True         |
|   97 | transitive                                  | False      | True           | ()            | True         |
|   98 | static                                      | False      | True           | ()            | True         |
|   99 | exports                                     | False      | True           | ()            | True         |
|  100 | to                                          | False      | True           | ()            | True         |
|  101 | opens                                       | False      | True           | ()            | True         |
|  102 | uses                                        | False      | True           | ()            | True         |
|  103 | provides                                    | False      | True           | ()            | True         |
|  104 | with                                        | False      | True           | ()            | True         |
|  105 | package                                     | False      | True           | ()            | True         |
|  106 | import                                      | False      | True           | ()            | True         |
|  107 | enum                                        | False      | True           | ()            | True         |
|  108 | public                                      | False      | True           | ()            | True         |
|  109 | protected                                   | False      | True           | ()            | True         |
|  110 | private                                     | False      | True           | ()            | True         |
|  111 | abstract                                    | False      | True           | ()            | True         |
|  112 | strictfp                                    | False      | True           | ()            | True         |
|  113 | native                                      | False      | True           | ()            | True         |
|  114 | transient                                   | False      | True           | ()            | True         |
|  115 | volatile                                    | False      | True           | ()            | True         |
|  116 | sealed                                      | False      | True           | ()            | True         |
|  117 | non-sealed                                  | False      | True           | ()            | True         |
|  118 | implements                                  | False      | True           | ()            | True         |
|  119 | permits                                     | False      | True           | ()            | True         |
|  120 | record                                      | False      | True           | ()            | True         |
|  121 | @interface                                  | False      | True           | ()            | True         |
|  122 | interface                                   | False      | True           | ()            | True         |
|  123 | byte                                        | False      | True           | ()            | True         |
|  124 | short                                       | False      | True           | ()            | True         |
|  125 | int                                         | False      | True           | ()            | True         |
|  126 | long                                        | False      | True           | ()            | True         |
|  127 | char                                        | False      | True           | ()            | True         |
|  128 | float                                       | False      | True           | ()            | True         |
|  129 | double                                      | False      | True           | ()            | True         |
|  130 | boolean\_type                               | True       | True           | ()            | True         |
|  131 | void\_type                                  | True       | True           | ()            | True         |
|  132 | ...                                         | False      | True           | ()            | True         |
|  133 | throws                                      | False      | True           | ()            | True         |
|  134 | this                                        | True       | True           | ()            | True         |
|  135 | super                                       | True       | True           | ()            | True         |
|  136 | line\_comment                               | True       | True           | ()            | True         |
|  137 | block\_comment                              | True       | True           | ()            | True         |
|  138 | program                                     | True       | True           | ()            | True         |
|  139 | \_toplevel\_statement                       | False      | False          | ()            | False        |
|  140 | \_literal                                   | False      | True           | ()            | False        |
|  141 | string\_literal                             | True       | True           | ()            | True         |
|  142 | \_string\_literal                           | False      | False          | ()            | False        |
|  143 | \_multiline\_string\_literal                | False      | False          | ()            | False        |
|  144 | multiline\_string\_fragment                 | True       | True           | ()            | True         |
|  145 | string\_interpolation                       | True       | True           | ()            | True         |
|  146 | \_escape\_sequence                          | False      | False          | ()            | False        |
|  147 | expression                                  | False      | True           | ()            | False        |
|  148 | cast\_expression                            | True       | True           | ()            | True         |
|  149 | assignment\_expression                      | True       | True           | ()            | True         |
|  150 | binary\_expression                          | True       | True           | ()            | True         |
|  151 | instanceof\_expression                      | True       | True           | ()            | True         |
|  152 | lambda\_expression                          | True       | True           | ()            | True         |
|  153 | inferred\_parameters                        | True       | True           | ()            | True         |
|  154 | ternary\_expression                         | True       | True           | ()            | True         |
|  155 | unary\_expression                           | True       | True           | ()            | True         |
|  156 | update\_expression                          | True       | True           | ()            | True         |
|  157 | primary\_expression                         | False      | True           | ()            | False        |
|  158 | array\_creation\_expression                 | True       | True           | ()            | True         |
|  159 | dimensions\_expr                            | True       | True           | ()            | True         |
|  160 | parenthesized\_expression                   | True       | True           | ()            | True         |
|  161 | class\_literal                              | True       | True           | ()            | True         |
|  162 | object\_creation\_expression                | True       | True           | ()            | True         |
|  163 | \_unqualified\_object\_creation\_expression | False      | False          | ()            | False        |
|  164 | field\_access                               | True       | True           | ()            | True         |
|  165 | template\_expression                        | True       | True           | ()            | True         |
|  166 | array\_access                               | True       | True           | ()            | True         |
|  167 | method\_invocation                          | True       | True           | ()            | True         |
|  168 | argument\_list                              | True       | True           | ()            | True         |
|  169 | method\_reference                           | True       | True           | ()            | True         |
|  170 | type\_arguments                             | True       | True           | ()            | True         |
|  171 | wildcard                                    | True       | True           | ()            | True         |
|  172 | \_wildcard\_bounds                          | False      | False          | ()            | False        |
|  173 | dimensions                                  | True       | True           | ()            | True         |
|  174 | switch\_expression                          | True       | True           | ()            | True         |
|  175 | switch\_block                               | True       | True           | ()            | True         |
|  176 | switch\_block\_statement\_group             | True       | True           | ()            | True         |
|  177 | switch\_rule                                | True       | True           | ()            | True         |
|  178 | switch\_label                               | True       | True           | ()            | True         |
|  179 | pattern                                     | True       | True           | ()            | True         |
|  180 | type\_pattern                               | True       | True           | ()            | True         |
|  181 | record\_pattern                             | True       | True           | ()            | True         |
|  182 | record\_pattern\_body                       | True       | True           | ()            | True         |
|  183 | record\_pattern\_component                  | True       | True           | ()            | True         |
|  184 | guard                                       | True       | True           | ()            | True         |
|  185 | statement                                   | False      | True           | ()            | False        |
|  186 | block                                       | True       | True           | ()            | True         |
|  187 | expression\_statement                       | True       | True           | ()            | True         |
|  188 | labeled\_statement                          | True       | True           | ()            | True         |
|  189 | assert\_statement                           | True       | True           | ()            | True         |
|  190 | do\_statement                               | True       | True           | ()            | True         |
|  191 | break\_statement                            | True       | True           | ()            | True         |
|  192 | continue\_statement                         | True       | True           | ()            | True         |
|  193 | return\_statement                           | True       | True           | ()            | True         |
|  194 | yield\_statement                            | True       | True           | ()            | True         |
|  195 | synchronized\_statement                     | True       | True           | ()            | True         |
|  196 | throw\_statement                            | True       | True           | ()            | True         |
|  197 | try\_statement                              | True       | True           | ()            | True         |
|  198 | catch\_clause                               | True       | True           | ()            | True         |
|  199 | catch\_formal\_parameter                    | True       | True           | ()            | True         |
|  200 | catch\_type                                 | True       | True           | ()            | True         |
|  201 | finally\_clause                             | True       | True           | ()            | True         |
|  202 | try\_with\_resources\_statement             | True       | True           | ()            | True         |
|  203 | resource\_specification                     | True       | True           | ()            | True         |
|  204 | resource                                    | True       | True           | ()            | True         |
|  205 | if\_statement                               | True       | True           | ()            | True         |
|  206 | while\_statement                            | True       | True           | ()            | True         |
|  207 | for\_statement                              | True       | True           | ()            | True         |
|  208 | enhanced\_for\_statement                    | True       | True           | ()            | True         |
|  209 | \_annotation                                | False      | False          | ()            | False        |
|  210 | marker\_annotation                          | True       | True           | ()            | True         |
|  211 | annotation                                  | True       | True           | ()            | True         |
|  212 | annotation\_argument\_list                  | True       | True           | ()            | True         |
|  213 | element\_value\_pair                        | True       | True           | ()            | True         |
|  214 | \_element\_value                            | False      | False          | ()            | False        |
|  215 | element\_value\_array\_initializer          | True       | True           | ()            | True         |
|  216 | declaration                                 | False      | True           | ()            | False        |
|  217 | module\_declaration                         | True       | True           | ()            | True         |
|  218 | module\_body                                | True       | True           | ()            | True         |
|  219 | module\_directive                           | False      | True           | ()            | False        |
|  220 | requires\_module\_directive                 | True       | True           | ()            | True         |
|  221 | requires\_modifier                          | True       | True           | ()            | True         |
|  222 | exports\_module\_directive                  | True       | True           | ()            | True         |
|  223 | opens\_module\_directive                    | True       | True           | ()            | True         |
|  224 | uses\_module\_directive                     | True       | True           | ()            | True         |
|  225 | provides\_module\_directive                 | True       | True           | ()            | True         |
|  226 | package\_declaration                        | True       | True           | ()            | True         |
|  227 | import\_declaration                         | True       | True           | ()            | True         |
|  228 | asterisk                                    | True       | True           | ()            | True         |
|  229 | enum\_declaration                           | True       | True           | ()            | True         |
|  230 | enum\_body                                  | True       | True           | ()            | True         |
|  231 | enum\_body\_declarations                    | True       | True           | ()            | True         |
|  232 | enum\_constant                              | True       | True           | ()            | True         |
|  233 | class\_declaration                          | True       | True           | ()            | True         |
|  234 | modifiers                                   | True       | True           | ()            | True         |
|  235 | type\_parameters                            | True       | True           | ()            | True         |
|  236 | type\_parameter                             | True       | True           | ()            | True         |
|  237 | type\_bound                                 | True       | True           | ()            | True         |
|  238 | superclass                                  | True       | True           | ()            | True         |
|  239 | super\_interfaces                           | True       | True           | ()            | True         |
|  240 | type\_list                                  | True       | True           | ()            | True         |
|  241 | permits                                     | True       | True           | ()            | True         |
|  242 | class\_body                                 | True       | True           | ()            | True         |
|  243 | static\_initializer                         | True       | True           | ()            | True         |
|  244 | constructor\_declaration                    | True       | True           | ()            | True         |
|  245 | \_constructor\_declarator                   | False      | False          | ()            | False        |
|  246 | constructor\_body                           | True       | True           | ()            | True         |
|  247 | explicit\_constructor\_invocation           | True       | True           | ()            | True         |
|  248 | scoped\_identifier                          | True       | True           | ()            | True         |
|  249 | field\_declaration                          | True       | True           | ()            | True         |
|  250 | record\_declaration                         | True       | True           | ()            | True         |
|  251 | annotation\_type\_declaration               | True       | True           | ()            | True         |
|  252 | annotation\_type\_body                      | True       | True           | ()            | True         |
|  253 | annotation\_type\_element\_declaration      | True       | True           | ()            | True         |
|  254 | \_default\_value                            | False      | False          | ()            | False        |
|  255 | interface\_declaration                      | True       | True           | ()            | True         |
|  256 | extends\_interfaces                         | True       | True           | ()            | True         |
|  257 | interface\_body                             | True       | True           | ()            | True         |
|  258 | constant\_declaration                       | True       | True           | ()            | True         |
|  259 | \_variable\_declarator\_list                | False      | False          | ()            | False        |
|  260 | variable\_declarator                        | True       | True           | ()            | True         |
|  261 | \_variable\_declarator\_id                  | False      | False          | ()            | False        |
|  262 | array\_initializer                          | True       | True           | ()            | True         |
|  263 | \_type                                      | False      | True           | ()            | False        |
|  264 | \_unannotated\_type                         | False      | True           | ()            | False        |
|  265 | annotated\_type                             | True       | True           | ()            | True         |
|  266 | scoped\_type\_identifier                    | True       | True           | ()            | True         |
|  267 | generic\_type                               | True       | True           | ()            | True         |
|  268 | array\_type                                 | True       | True           | ()            | True         |
|  269 | integral\_type                              | True       | True           | ()            | True         |
|  270 | floating\_point\_type                       | True       | True           | ()            | True         |
|  271 | \_method\_header                            | False      | False          | ()            | False        |
|  272 | \_method\_declarator                        | False      | False          | ()            | False        |
|  273 | formal\_parameters                          | True       | True           | ()            | True         |
|  274 | formal\_parameter                           | True       | True           | ()            | True         |
|  275 | receiver\_parameter                         | True       | True           | ()            | True         |
|  276 | spread\_parameter                           | True       | True           | ()            | True         |
|  277 | throws                                      | True       | True           | ()            | True         |
|  278 | local\_variable\_declaration                | True       | True           | ()            | True         |
|  279 | method\_declaration                         | True       | True           | ()            | True         |
|  280 | compact\_constructor\_declaration           | True       | True           | ()            | True         |
|  281 | \_reserved\_identifier                      | False      | False          | ()            | False        |
|  282 | program\_repeat1                            | False      | False          | ()            | False        |
|  283 | \_string\_literal\_repeat1                  | False      | False          | ()            | False        |
|  284 | \_multiline\_string\_literal\_repeat1       | False      | False          | ()            | False        |
|  285 | cast\_expression\_repeat1                   | False      | False          | ()            | False        |
|  286 | inferred\_parameters\_repeat1               | False      | False          | ()            | False        |
|  287 | array\_creation\_expression\_repeat1        | False      | False          | ()            | False        |
|  288 | array\_creation\_expression\_repeat2        | False      | False          | ()            | False        |
|  289 | argument\_list\_repeat1                     | False      | False          | ()            | False        |
|  290 | type\_arguments\_repeat1                    | False      | False          | ()            | False        |
|  291 | dimensions\_repeat1                         | False      | False          | ()            | False        |
|  292 | switch\_block\_repeat1                      | False      | False          | ()            | False        |
|  293 | switch\_block\_repeat2                      | False      | False          | ()            | False        |
|  294 | switch\_block\_statement\_group\_repeat1    | False      | False          | ()            | False        |
|  295 | switch\_block\_statement\_group\_repeat2    | False      | False          | ()            | False        |
|  296 | record\_pattern\_body\_repeat1              | False      | False          | ()            | False        |
|  297 | try\_statement\_repeat1                     | False      | False          | ()            | False        |
|  298 | catch\_type\_repeat1                        | False      | False          | ()            | False        |
|  299 | resource\_specification\_repeat1            | False      | False          | ()            | False        |
|  300 | for\_statement\_repeat1                     | False      | False          | ()            | False        |
|  301 | for\_statement\_repeat2                     | False      | False          | ()            | False        |
|  302 | annotation\_argument\_list\_repeat1         | False      | False          | ()            | False        |
|  303 | element\_value\_array\_initializer\_repeat1 | False      | False          | ()            | False        |
|  304 | module\_body\_repeat1                       | False      | False          | ()            | False        |
|  305 | requires\_module\_directive\_repeat1        | False      | False          | ()            | False        |
|  306 | exports\_module\_directive\_repeat1         | False      | False          | ()            | False        |
|  307 | provides\_module\_directive\_repeat1        | False      | False          | ()            | False        |
|  308 | enum\_body\_repeat1                         | False      | False          | ()            | False        |
|  309 | enum\_body\_declarations\_repeat1           | False      | False          | ()            | False        |
|  310 | modifiers\_repeat1                          | False      | False          | ()            | False        |
|  311 | type\_parameters\_repeat1                   | False      | False          | ()            | False        |
|  312 | type\_bound\_repeat1                        | False      | False          | ()            | False        |
|  313 | type\_list\_repeat1                         | False      | False          | ()            | False        |
|  314 | annotation\_type\_body\_repeat1             | False      | False          | ()            | False        |
|  315 | interface\_body\_repeat1                    | False      | False          | ()            | False        |
|  316 | \_variable\_declarator\_list\_repeat1       | False      | False          | ()            | False        |
|  317 | array\_initializer\_repeat1                 | False      | False          | ()            | False        |
|  318 | formal\_parameters\_repeat1                 | False      | False          | ()            | False        |
|  319 | receiver\_parameter\_repeat1                | False      | False          | ()            | False        |
|  320 | type\_identifier                            | True       | True           | ()            | True         |

## Fields

|   id | name                |
|------|---------------------|
|    0 | `None`              |
|    1 | alternative         |
|    2 | arguments           |
|    3 | array               |
|    4 | body                |
|    5 | condition           |
|    6 | consequence         |
|    7 | constructor         |
|    8 | declarator          |
|    9 | dimensions          |
|   10 | element             |
|   11 | field               |
|   12 | index               |
|   13 | init                |
|   14 | interfaces          |
|   15 | key                 |
|   16 | left                |
|   17 | modifiers           |
|   18 | module              |
|   19 | modules             |
|   20 | name                |
|   21 | object              |
|   22 | operand             |
|   23 | operator            |
|   24 | package             |
|   25 | parameters          |
|   26 | pattern             |
|   27 | permits             |
|   28 | provided            |
|   29 | provider            |
|   30 | resources           |
|   31 | right               |
|   32 | scope               |
|   33 | superclass          |
|   34 | template\_argument  |
|   35 | template\_processor |
|   36 | type                |
|   37 | type\_arguments     |
|   38 | type\_parameters    |
|   39 | update              |


# JAVASCRIPT

- Language: javascript
- ABI version: 15
- File name extensions: ['.js', '.jsx', '.mjs', '.cjs']
- File name patterns: []
- Node kinds count: 265
    - Anonymous node count: 142
    - Visible node count: 231
    - Supertype node count: 236
- Field count: 36

## Node kinds

|   id | name                                     | is_named   | is_supertype   | subtype_ids                                                                                                  | is_visible   |
|------|------------------------------------------|------------|----------------|--------------------------------------------------------------------------------------------------------------|--------------|
|    0 | end                                      | False      | False          | ()                                                                                                           | False        |
|    1 | identifier                               | True       | True           | ()                                                                                                           | True         |
|    2 | hash\_bang\_line                         | True       | True           | ()                                                                                                           | True         |
|    3 | export                                   | False      | True           | ()                                                                                                           | True         |
|    4 | \*                                       | False      | True           | ()                                                                                                           | True         |
|    5 | default                                  | False      | True           | ()                                                                                                           | True         |
|    6 | as                                       | False      | True           | ()                                                                                                           | True         |
|    7 | {                                        | False      | True           | ()                                                                                                           | True         |
|    8 | ,                                        | False      | True           | ()                                                                                                           | True         |
|    9 | }                                        | False      | True           | ()                                                                                                           | True         |
|   10 | import                                   | False      | True           | ()                                                                                                           | True         |
|   11 | from                                     | False      | True           | ()                                                                                                           | True         |
|   12 | with                                     | False      | True           | ()                                                                                                           | True         |
|   13 | var                                      | False      | True           | ()                                                                                                           | True         |
|   14 | let                                      | False      | True           | ()                                                                                                           | True         |
|   15 | const                                    | False      | True           | ()                                                                                                           | True         |
|   16 | using                                    | False      | True           | ()                                                                                                           | True         |
|   17 | await                                    | False      | True           | ()                                                                                                           | True         |
|   18 | of                                       | False      | True           | ()                                                                                                           | True         |
|   19 | else                                     | False      | True           | ()                                                                                                           | True         |
|   20 | if                                       | False      | True           | ()                                                                                                           | True         |
|   21 | switch                                   | False      | True           | ()                                                                                                           | True         |
|   22 | for                                      | False      | True           | ()                                                                                                           | True         |
|   23 | (                                        | False      | True           | ()                                                                                                           | True         |
|   24 | ;                                        | False      | True           | ()                                                                                                           | True         |
|   25 | )                                        | False      | True           | ()                                                                                                           | True         |
|   26 | in                                       | False      | True           | ()                                                                                                           | True         |
|   27 | while                                    | False      | True           | ()                                                                                                           | True         |
|   28 | do                                       | False      | True           | ()                                                                                                           | True         |
|   29 | try                                      | False      | True           | ()                                                                                                           | True         |
|   30 | break                                    | False      | True           | ()                                                                                                           | True         |
|   31 | continue                                 | False      | True           | ()                                                                                                           | True         |
|   32 | debugger                                 | False      | True           | ()                                                                                                           | True         |
|   33 | return                                   | False      | True           | ()                                                                                                           | True         |
|   34 | throw                                    | False      | True           | ()                                                                                                           | True         |
|   35 | :                                        | False      | True           | ()                                                                                                           | True         |
|   36 | case                                     | False      | True           | ()                                                                                                           | True         |
|   37 | catch                                    | False      | True           | ()                                                                                                           | True         |
|   38 | finally                                  | False      | True           | ()                                                                                                           | True         |
|   39 | yield                                    | False      | True           | ()                                                                                                           | True         |
|   40 | =                                        | False      | True           | ()                                                                                                           | True         |
|   41 | [                                        | False      | True           | ()                                                                                                           | True         |
|   42 | ]                                        | False      | True           | ()                                                                                                           | True         |
|   43 | html\_character\_reference               | True       | True           | ()                                                                                                           | True         |
|   44 | &lt;                                     | False      | True           | ()                                                                                                           | True         |
|   45 | &gt;                                     | False      | True           | ()                                                                                                           | True         |
|   46 | identifier                               | True       | True           | ()                                                                                                           | True         |
|   47 | .                                        | False      | True           | ()                                                                                                           | True         |
|   48 | &lt;/                                    | False      | True           | ()                                                                                                           | True         |
|   49 | /&gt;                                    | False      | True           | ()                                                                                                           | True         |
|   50 | "                                        | False      | True           | ()                                                                                                           | True         |
|   51 | '                                        | False      | True           | ()                                                                                                           | True         |
|   52 | string\_fragment                         | True       | True           | ()                                                                                                           | True         |
|   53 | string\_fragment                         | True       | True           | ()                                                                                                           | True         |
|   54 | class                                    | False      | True           | ()                                                                                                           | True         |
|   55 | extends                                  | False      | True           | ()                                                                                                           | True         |
|   56 | async                                    | False      | True           | ()                                                                                                           | True         |
|   57 | function                                 | False      | True           | ()                                                                                                           | True         |
|   58 | =&gt;                                    | False      | True           | ()                                                                                                           | True         |
|   59 | optional\_chain                          | True       | True           | ()                                                                                                           | True         |
|   60 | new                                      | False      | True           | ()                                                                                                           | True         |
|   61 | +=                                       | False      | True           | ()                                                                                                           | True         |
|   62 | -=                                       | False      | True           | ()                                                                                                           | True         |
|   63 | \*=                                      | False      | True           | ()                                                                                                           | True         |
|   64 | /=                                       | False      | True           | ()                                                                                                           | True         |
|   65 | %=                                       | False      | True           | ()                                                                                                           | True         |
|   66 | ^=                                       | False      | True           | ()                                                                                                           | True         |
|   67 | &amp;=                                   | False      | True           | ()                                                                                                           | True         |
|   68 | &#124;=                                  | False      | True           | ()                                                                                                           | True         |
|   69 | &gt;&gt;=                                | False      | True           | ()                                                                                                           | True         |
|   70 | &gt;&gt;&gt;=                            | False      | True           | ()                                                                                                           | True         |
|   71 | &lt;&lt;=                                | False      | True           | ()                                                                                                           | True         |
|   72 | \*\*=                                    | False      | True           | ()                                                                                                           | True         |
|   73 | &amp;&amp;=                              | False      | True           | ()                                                                                                           | True         |
|   74 | &#124;&#124;=                            | False      | True           | ()                                                                                                           | True         |
|   75 | ??=                                      | False      | True           | ()                                                                                                           | True         |
|   76 | ...                                      | False      | True           | ()                                                                                                           | True         |
|   77 | &amp;&amp;                               | False      | True           | ()                                                                                                           | True         |
|   78 | &#124;&#124;                             | False      | True           | ()                                                                                                           | True         |
|   79 | &gt;&gt;                                 | False      | True           | ()                                                                                                           | True         |
|   80 | &gt;&gt;&gt;                             | False      | True           | ()                                                                                                           | True         |
|   81 | &lt;&lt;                                 | False      | True           | ()                                                                                                           | True         |
|   82 | &amp;                                    | False      | True           | ()                                                                                                           | True         |
|   83 | ^                                        | False      | True           | ()                                                                                                           | True         |
|   84 | &#124;                                   | False      | True           | ()                                                                                                           | True         |
|   85 | +                                        | False      | True           | ()                                                                                                           | True         |
|   86 | -                                        | False      | True           | ()                                                                                                           | True         |
|   87 | /                                        | False      | True           | ()                                                                                                           | True         |
|   88 | %                                        | False      | True           | ()                                                                                                           | True         |
|   89 | \*\*                                     | False      | True           | ()                                                                                                           | True         |
|   90 | &lt;=                                    | False      | True           | ()                                                                                                           | True         |
|   91 | ==                                       | False      | True           | ()                                                                                                           | True         |
|   92 | ===                                      | False      | True           | ()                                                                                                           | True         |
|   93 | !=                                       | False      | True           | ()                                                                                                           | True         |
|   94 | !==                                      | False      | True           | ()                                                                                                           | True         |
|   95 | &gt;=                                    | False      | True           | ()                                                                                                           | True         |
|   96 | ??                                       | False      | True           | ()                                                                                                           | True         |
|   97 | instanceof                               | False      | True           | ()                                                                                                           | True         |
|   98 | !                                        | False      | True           | ()                                                                                                           | True         |
|   99 | ~                                        | False      | True           | ()                                                                                                           | True         |
|  100 | typeof                                   | False      | True           | ()                                                                                                           | True         |
|  101 | void                                     | False      | True           | ()                                                                                                           | True         |
|  102 | delete                                   | False      | True           | ()                                                                                                           | True         |
|  103 | ++                                       | False      | True           | ()                                                                                                           | True         |
|  104 | --                                       | False      | True           | ()                                                                                                           | True         |
|  105 | string\_fragment                         | True       | True           | ()                                                                                                           | True         |
|  106 | string\_fragment                         | True       | True           | ()                                                                                                           | True         |
|  107 | escape\_sequence                         | True       | True           | ()                                                                                                           | True         |
|  108 | comment                                  | True       | True           | ()                                                                                                           | True         |
|  109 | \`                                       | False      | True           | ()                                                                                                           | True         |
|  110 | ${                                       | False      | True           | ()                                                                                                           | True         |
|  111 | /                                        | False      | True           | ()                                                                                                           | True         |
|  112 | regex\_pattern                           | True       | True           | ()                                                                                                           | True         |
|  113 | regex\_flags                             | True       | True           | ()                                                                                                           | True         |
|  114 | number                                   | True       | True           | ()                                                                                                           | True         |
|  115 | private\_property\_identifier            | True       | True           | ()                                                                                                           | True         |
|  116 | target                                   | False      | True           | ()                                                                                                           | True         |
|  117 | meta                                     | False      | True           | ()                                                                                                           | True         |
|  118 | this                                     | True       | True           | ()                                                                                                           | True         |
|  119 | super                                    | True       | True           | ()                                                                                                           | True         |
|  120 | true                                     | True       | True           | ()                                                                                                           | True         |
|  121 | false                                    | True       | True           | ()                                                                                                           | True         |
|  122 | null                                     | True       | True           | ()                                                                                                           | True         |
|  123 | undefined                                | True       | True           | ()                                                                                                           | True         |
|  124 | @                                        | False      | True           | ()                                                                                                           | True         |
|  125 | static                                   | False      | True           | ()                                                                                                           | True         |
|  126 | static get                               | False      | True           | ()                                                                                                           | True         |
|  127 | get                                      | False      | True           | ()                                                                                                           | True         |
|  128 | set                                      | False      | True           | ()                                                                                                           | True         |
|  129 | \_automatic\_semicolon                   | False      | False          | ()                                                                                                           | False        |
|  130 | string\_fragment                         | True       | True           | ()                                                                                                           | True         |
|  131 | ?                                        | False      | True           | ()                                                                                                           | True         |
|  132 | html\_comment                            | True       | True           | ()                                                                                                           | True         |
|  133 | jsx\_text                                | True       | True           | ()                                                                                                           | True         |
|  134 | program                                  | True       | True           | ()                                                                                                           | True         |
|  135 | export\_statement                        | True       | True           | ()                                                                                                           | True         |
|  136 | namespace\_export                        | True       | True           | ()                                                                                                           | True         |
|  137 | export\_clause                           | True       | True           | ()                                                                                                           | True         |
|  138 | export\_specifier                        | True       | True           | ()                                                                                                           | True         |
|  139 | \_module\_export\_name                   | False      | False          | ()                                                                                                           | False        |
|  140 | declaration                              | False      | True           | (198, 201, 203, 152, 153, 151)                                                                               | False        |
|  141 | import                                   | True       | True           | ()                                                                                                           | True         |
|  142 | import\_statement                        | True       | True           | ()                                                                                                           | True         |
|  143 | import\_clause                           | True       | True           | ()                                                                                                           | True         |
|  144 | \_from\_clause                           | False      | False          | ()                                                                                                           | False        |
|  145 | namespace\_import                        | True       | True           | ()                                                                                                           | True         |
|  146 | named\_imports                           | True       | True           | ()                                                                                                           | True         |
|  147 | import\_specifier                        | True       | True           | ()                                                                                                           | True         |
|  148 | import\_attribute                        | True       | True           | ()                                                                                                           | True         |
|  149 | statement                                | False      | True           | (166, 167, 168, 140, 163, 171, 135, 150, 160, 159, 157, 142, 172, 169, 155, 158, 170, 164, 162, 165)         | False        |
|  150 | expression\_statement                    | True       | True           | ()                                                                                                           | True         |
|  151 | variable\_declaration                    | True       | True           | ()                                                                                                           | True         |
|  152 | lexical\_declaration                     | True       | True           | ()                                                                                                           | True         |
|  153 | using\_declaration                       | True       | True           | ()                                                                                                           | True         |
|  154 | variable\_declarator                     | True       | True           | ()                                                                                                           | True         |
|  155 | statement\_block                         | True       | True           | ()                                                                                                           | True         |
|  156 | else\_clause                             | True       | True           | ()                                                                                                           | True         |
|  157 | if\_statement                            | True       | True           | ()                                                                                                           | True         |
|  158 | switch\_statement                        | True       | True           | ()                                                                                                           | True         |
|  159 | for\_statement                           | True       | True           | ()                                                                                                           | True         |
|  160 | for\_in\_statement                       | True       | True           | ()                                                                                                           | True         |
|  161 | \_for\_header                            | False      | False          | ()                                                                                                           | False        |
|  162 | while\_statement                         | True       | True           | ()                                                                                                           | True         |
|  163 | do\_statement                            | True       | True           | ()                                                                                                           | True         |
|  164 | try\_statement                           | True       | True           | ()                                                                                                           | True         |
|  165 | with\_statement                          | True       | True           | ()                                                                                                           | True         |
|  166 | break\_statement                         | True       | True           | ()                                                                                                           | True         |
|  167 | continue\_statement                      | True       | True           | ()                                                                                                           | True         |
|  168 | debugger\_statement                      | True       | True           | ()                                                                                                           | True         |
|  169 | return\_statement                        | True       | True           | ()                                                                                                           | True         |
|  170 | throw\_statement                         | True       | True           | ()                                                                                                           | True         |
|  171 | empty\_statement                         | True       | True           | ()                                                                                                           | True         |
|  172 | labeled\_statement                       | True       | True           | ()                                                                                                           | True         |
|  173 | switch\_body                             | True       | True           | ()                                                                                                           | True         |
|  174 | switch\_case                             | True       | True           | ()                                                                                                           | True         |
|  175 | switch\_default                          | True       | True           | ()                                                                                                           | True         |
|  176 | catch\_clause                            | True       | True           | ()                                                                                                           | True         |
|  177 | finally\_clause                          | True       | True           | ()                                                                                                           | True         |
|  178 | parenthesized\_expression                | True       | True           | ()                                                                                                           | True         |
|  179 | expression                               | False      | True           | (210, 212, 207, 217, 188, 194, 206, 180, 216, 218, 219, 181)                                                 | False        |
|  180 | primary\_expression                      | False      | True           | (186, 204, 205, 197, 121, 200, 202, 1, 208, 225, 122, 114, 182, 178, 224, 221, 209, 119, 222, 118, 120, 123) | False        |
|  181 | yield\_expression                        | True       | True           | ()                                                                                                           | True         |
|  182 | object                                   | True       | True           | ()                                                                                                           | True         |
|  183 | object\_pattern                          | True       | True           | ()                                                                                                           | True         |
|  184 | assignment\_pattern                      | True       | True           | ()                                                                                                           | True         |
|  185 | object\_assignment\_pattern              | True       | True           | ()                                                                                                           | True         |
|  186 | array                                    | True       | True           | ()                                                                                                           | True         |
|  187 | array\_pattern                           | True       | True           | ()                                                                                                           | True         |
|  188 | jsx\_element                             | True       | True           | ()                                                                                                           | True         |
|  189 | jsx\_expression                          | True       | True           | ()                                                                                                           | True         |
|  190 | jsx\_opening\_element                    | True       | True           | ()                                                                                                           | True         |
|  191 | member\_expression                       | True       | True           | ()                                                                                                           | True         |
|  192 | jsx\_namespace\_name                     | True       | True           | ()                                                                                                           | True         |
|  193 | jsx\_closing\_element                    | True       | True           | ()                                                                                                           | True         |
|  194 | jsx\_self\_closing\_element              | True       | True           | ()                                                                                                           | True         |
|  195 | jsx\_attribute                           | True       | True           | ()                                                                                                           | True         |
|  196 | string                                   | True       | True           | ()                                                                                                           | True         |
|  197 | class                                    | True       | True           | ()                                                                                                           | True         |
|  198 | class\_declaration                       | True       | True           | ()                                                                                                           | True         |
|  199 | class\_heritage                          | True       | True           | ()                                                                                                           | True         |
|  200 | function\_expression                     | True       | True           | ()                                                                                                           | True         |
|  201 | function\_declaration                    | True       | True           | ()                                                                                                           | True         |
|  202 | generator\_function                      | True       | True           | ()                                                                                                           | True         |
|  203 | generator\_function\_declaration         | True       | True           | ()                                                                                                           | True         |
|  204 | arrow\_function                          | True       | True           | ()                                                                                                           | True         |
|  205 | call\_expression                         | True       | True           | ()                                                                                                           | True         |
|  206 | new\_expression                          | True       | True           | ()                                                                                                           | True         |
|  207 | await\_expression                        | True       | True           | ()                                                                                                           | True         |
|  208 | member\_expression                       | True       | True           | ()                                                                                                           | True         |
|  209 | subscript\_expression                    | True       | True           | ()                                                                                                           | True         |
|  210 | assignment\_expression                   | True       | True           | ()                                                                                                           | True         |
|  211 | \_augmented\_assignment\_lhs             | False      | False          | ()                                                                                                           | False        |
|  212 | augmented\_assignment\_expression        | True       | True           | ()                                                                                                           | True         |
|  213 | \_initializer                            | False      | False          | ()                                                                                                           | False        |
|  214 | \_destructuring\_pattern                 | False      | False          | ()                                                                                                           | False        |
|  215 | spread\_element                          | True       | True           | ()                                                                                                           | True         |
|  216 | ternary\_expression                      | True       | True           | ()                                                                                                           | True         |
|  217 | binary\_expression                       | True       | True           | ()                                                                                                           | True         |
|  218 | unary\_expression                        | True       | True           | ()                                                                                                           | True         |
|  219 | update\_expression                       | True       | True           | ()                                                                                                           | True         |
|  220 | sequence\_expression                     | True       | True           | ()                                                                                                           | True         |
|  221 | string                                   | True       | True           | ()                                                                                                           | True         |
|  222 | template\_string                         | True       | True           | ()                                                                                                           | True         |
|  223 | template\_substitution                   | True       | True           | ()                                                                                                           | True         |
|  224 | regex                                    | True       | True           | ()                                                                                                           | True         |
|  225 | meta\_property                           | True       | True           | ()                                                                                                           | True         |
|  226 | arguments                                | True       | True           | ()                                                                                                           | True         |
|  227 | decorator                                | True       | True           | ()                                                                                                           | True         |
|  228 | member\_expression                       | True       | True           | ()                                                                                                           | True         |
|  229 | call\_expression                         | True       | True           | ()                                                                                                           | True         |
|  230 | class\_body                              | True       | True           | ()                                                                                                           | True         |
|  231 | field\_definition                        | True       | True           | ()                                                                                                           | True         |
|  232 | formal\_parameters                       | True       | True           | ()                                                                                                           | True         |
|  233 | class\_static\_block                     | True       | True           | ()                                                                                                           | True         |
|  234 | pattern                                  | False      | True           | (187, 1, 208, 183, 235, 209, 123)                                                                            | False        |
|  235 | rest\_pattern                            | True       | True           | ()                                                                                                           | True         |
|  236 | method\_definition                       | True       | True           | ()                                                                                                           | True         |
|  237 | pair                                     | True       | True           | ()                                                                                                           | True         |
|  238 | pair\_pattern                            | True       | True           | ()                                                                                                           | True         |
|  239 | \_property\_name                         | False      | False          | ()                                                                                                           | False        |
|  240 | computed\_property\_name                 | True       | True           | ()                                                                                                           | True         |
|  241 | program\_repeat1                         | False      | False          | ()                                                                                                           | False        |
|  242 | export\_statement\_repeat1               | False      | False          | ()                                                                                                           | False        |
|  243 | export\_clause\_repeat1                  | False      | False          | ()                                                                                                           | False        |
|  244 | named\_imports\_repeat1                  | False      | False          | ()                                                                                                           | False        |
|  245 | variable\_declaration\_repeat1           | False      | False          | ()                                                                                                           | False        |
|  246 | switch\_body\_repeat1                    | False      | False          | ()                                                                                                           | False        |
|  247 | object\_repeat1                          | False      | False          | ()                                                                                                           | False        |
|  248 | object\_pattern\_repeat1                 | False      | False          | ()                                                                                                           | False        |
|  249 | array\_repeat1                           | False      | False          | ()                                                                                                           | False        |
|  250 | array\_pattern\_repeat1                  | False      | False          | ()                                                                                                           | False        |
|  251 | jsx\_element\_repeat1                    | False      | False          | ()                                                                                                           | False        |
|  252 | jsx\_opening\_element\_repeat1           | False      | False          | ()                                                                                                           | False        |
|  253 | \_jsx\_string\_repeat1                   | False      | False          | ()                                                                                                           | False        |
|  254 | \_jsx\_string\_repeat2                   | False      | False          | ()                                                                                                           | False        |
|  255 | sequence\_expression\_repeat1            | False      | False          | ()                                                                                                           | False        |
|  256 | string\_repeat1                          | False      | False          | ()                                                                                                           | False        |
|  257 | string\_repeat2                          | False      | False          | ()                                                                                                           | False        |
|  258 | template\_string\_repeat1                | False      | False          | ()                                                                                                           | False        |
|  259 | class\_body\_repeat1                     | False      | False          | ()                                                                                                           | False        |
|  260 | formal\_parameters\_repeat1              | False      | False          | ()                                                                                                           | False        |
|  261 | property\_identifier                     | True       | True           | ()                                                                                                           | True         |
|  262 | shorthand\_property\_identifier          | True       | True           | ()                                                                                                           | True         |
|  263 | shorthand\_property\_identifier\_pattern | True       | True           | ()                                                                                                           | True         |
|  264 | statement\_identifier                    | True       | True           | ()                                                                                                           | True         |

## Fields

|   id | name            |
|------|-----------------|
|    0 | `None`          |
|    1 | alias           |
|    2 | alternative     |
|    3 | argument        |
|    4 | arguments       |
|    5 | attribute       |
|    6 | body            |
|    7 | close\_tag      |
|    8 | condition       |
|    9 | consequence     |
|   10 | constructor     |
|   11 | declaration     |
|   12 | decorator       |
|   13 | finalizer       |
|   14 | flags           |
|   15 | function        |
|   16 | handler         |
|   17 | increment       |
|   18 | index           |
|   19 | initializer     |
|   20 | key             |
|   21 | kind            |
|   22 | label           |
|   23 | left            |
|   24 | member          |
|   25 | name            |
|   26 | object          |
|   27 | open\_tag       |
|   28 | operator        |
|   29 | optional\_chain |
|   30 | parameter       |
|   31 | parameters      |
|   32 | pattern         |
|   33 | property        |
|   34 | right           |
|   35 | source          |


# JSON

- Language: json
- ABI version: 14
- File name extensions: ['.json']
- File name patterns: []
- Node kinds count: 25
    - Anonymous node count: 13
    - Visible node count: 19
    - Supertype node count: 20
- Field count: 2

## Node kinds

|   id | name              | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|-------------------|------------|----------------|---------------|--------------|
|    0 | end               | False      | False          | ()            | False        |
|    1 | {                 | False      | True           | ()            | True         |
|    2 | ,                 | False      | True           | ()            | True         |
|    3 | }                 | False      | True           | ()            | True         |
|    4 | :                 | False      | True           | ()            | True         |
|    5 | [                 | False      | True           | ()            | True         |
|    6 | ]                 | False      | True           | ()            | True         |
|    7 | "                 | False      | True           | ()            | True         |
|    8 | string\_content   | True       | True           | ()            | True         |
|    9 | escape\_sequence  | True       | True           | ()            | True         |
|   10 | number            | True       | True           | ()            | True         |
|   11 | true              | True       | True           | ()            | True         |
|   12 | false             | True       | True           | ()            | True         |
|   13 | null              | True       | True           | ()            | True         |
|   14 | comment           | True       | True           | ()            | True         |
|   15 | document          | True       | True           | ()            | True         |
|   16 | \_value           | False      | True           | ()            | False        |
|   17 | object            | True       | True           | ()            | True         |
|   18 | pair              | True       | True           | ()            | True         |
|   19 | array             | True       | True           | ()            | True         |
|   20 | string            | True       | True           | ()            | True         |
|   21 | \_string\_content | False      | False          | ()            | False        |
|   22 | document\_repeat1 | False      | False          | ()            | False        |
|   23 | object\_repeat1   | False      | False          | ()            | False        |
|   24 | array\_repeat1    | False      | False          | ()            | False        |

## Fields

|   id | name   |
|------|--------|
|    0 | `None` |
|    1 | key    |


# PYTHON

- Language: python
- ABI version: 15
- File name extensions: ['.py', '.pyw']
- File name patterns: []
- Node kinds count: 274
    - Anonymous node count: 146
    - Visible node count: 218
    - Supertype node count: 222
- Field count: 32

## Node kinds

|   id | name                                  | is_named   | is_supertype   | subtype_ids                                                                                                           | is_visible   |
|------|---------------------------------------|------------|----------------|-----------------------------------------------------------------------------------------------------------------------|--------------|
|    0 | end                                   | False      | False          | ()                                                                                                                    | False        |
|    1 | identifier                            | True       | True           | ()                                                                                                                    | True         |
|    2 | ;                                     | False      | True           | ()                                                                                                                    | True         |
|    3 | import                                | False      | True           | ()                                                                                                                    | True         |
|    4 | .                                     | False      | True           | ()                                                                                                                    | True         |
|    5 | from                                  | False      | True           | ()                                                                                                                    | True         |
|    6 | \_\_future\_\_                        | False      | True           | ()                                                                                                                    | True         |
|    7 | (                                     | False      | True           | ()                                                                                                                    | True         |
|    8 | )                                     | False      | True           | ()                                                                                                                    | True         |
|    9 | ,                                     | False      | True           | ()                                                                                                                    | True         |
|   10 | as                                    | False      | True           | ()                                                                                                                    | True         |
|   11 | \*                                    | False      | True           | ()                                                                                                                    | True         |
|   12 | print                                 | False      | True           | ()                                                                                                                    | True         |
|   13 | &gt;&gt;                              | False      | True           | ()                                                                                                                    | True         |
|   14 | assert                                | False      | True           | ()                                                                                                                    | True         |
|   15 | :=                                    | False      | True           | ()                                                                                                                    | True         |
|   16 | return                                | False      | True           | ()                                                                                                                    | True         |
|   17 | del                                   | False      | True           | ()                                                                                                                    | True         |
|   18 | raise                                 | False      | True           | ()                                                                                                                    | True         |
|   19 | pass                                  | False      | True           | ()                                                                                                                    | True         |
|   20 | break                                 | False      | True           | ()                                                                                                                    | True         |
|   21 | continue                              | False      | True           | ()                                                                                                                    | True         |
|   22 | if                                    | False      | True           | ()                                                                                                                    | True         |
|   23 | :                                     | False      | True           | ()                                                                                                                    | True         |
|   24 | elif                                  | False      | True           | ()                                                                                                                    | True         |
|   25 | else                                  | False      | True           | ()                                                                                                                    | True         |
|   26 | match                                 | False      | True           | ()                                                                                                                    | True         |
|   27 | case                                  | False      | True           | ()                                                                                                                    | True         |
|   28 | async                                 | False      | True           | ()                                                                                                                    | True         |
|   29 | for                                   | False      | True           | ()                                                                                                                    | True         |
|   30 | in                                    | False      | True           | ()                                                                                                                    | True         |
|   31 | while                                 | False      | True           | ()                                                                                                                    | True         |
|   32 | try                                   | False      | True           | ()                                                                                                                    | True         |
|   33 | except                                | False      | True           | ()                                                                                                                    | True         |
|   34 | \*                                    | False      | True           | ()                                                                                                                    | True         |
|   35 | finally                               | False      | True           | ()                                                                                                                    | True         |
|   36 | with                                  | False      | True           | ()                                                                                                                    | True         |
|   37 | def                                   | False      | True           | ()                                                                                                                    | True         |
|   38 | -&gt;                                 | False      | True           | ()                                                                                                                    | True         |
|   39 | \*\*                                  | False      | True           | ()                                                                                                                    | True         |
|   40 | global                                | False      | True           | ()                                                                                                                    | True         |
|   41 | nonlocal                              | False      | True           | ()                                                                                                                    | True         |
|   42 | exec                                  | False      | True           | ()                                                                                                                    | True         |
|   43 | type                                  | False      | True           | ()                                                                                                                    | True         |
|   44 | =                                     | False      | True           | ()                                                                                                                    | True         |
|   45 | class                                 | False      | True           | ()                                                                                                                    | True         |
|   46 | [                                     | False      | True           | ()                                                                                                                    | True         |
|   47 | ]                                     | False      | True           | ()                                                                                                                    | True         |
|   48 | @                                     | False      | True           | ()                                                                                                                    | True         |
|   49 | -                                     | False      | True           | ()                                                                                                                    | True         |
|   50 | \_                                    | False      | True           | ()                                                                                                                    | True         |
|   51 | &#124;                                | False      | True           | ()                                                                                                                    | True         |
|   52 | {                                     | False      | True           | ()                                                                                                                    | True         |
|   53 | }                                     | False      | True           | ()                                                                                                                    | True         |
|   54 | +                                     | False      | True           | ()                                                                                                                    | True         |
|   55 | not                                   | False      | True           | ()                                                                                                                    | True         |
|   56 | and                                   | False      | True           | ()                                                                                                                    | True         |
|   57 | or                                    | False      | True           | ()                                                                                                                    | True         |
|   58 | /                                     | False      | True           | ()                                                                                                                    | True         |
|   59 | %                                     | False      | True           | ()                                                                                                                    | True         |
|   60 | //                                    | False      | True           | ()                                                                                                                    | True         |
|   61 | &amp;                                 | False      | True           | ()                                                                                                                    | True         |
|   62 | ^                                     | False      | True           | ()                                                                                                                    | True         |
|   63 | &lt;&lt;                              | False      | True           | ()                                                                                                                    | True         |
|   64 | ~                                     | False      | True           | ()                                                                                                                    | True         |
|   65 | is                                    | False      | True           | ()                                                                                                                    | True         |
|   66 | &lt;                                  | False      | True           | ()                                                                                                                    | True         |
|   67 | &lt;=                                 | False      | True           | ()                                                                                                                    | True         |
|   68 | ==                                    | False      | True           | ()                                                                                                                    | True         |
|   69 | !=                                    | False      | True           | ()                                                                                                                    | True         |
|   70 | &gt;=                                 | False      | True           | ()                                                                                                                    | True         |
|   71 | &gt;                                  | False      | True           | ()                                                                                                                    | True         |
|   72 | &lt;&gt;                              | False      | True           | ()                                                                                                                    | True         |
|   73 | lambda                                | False      | True           | ()                                                                                                                    | True         |
|   74 | +=                                    | False      | True           | ()                                                                                                                    | True         |
|   75 | -=                                    | False      | True           | ()                                                                                                                    | True         |
|   76 | \*=                                   | False      | True           | ()                                                                                                                    | True         |
|   77 | /=                                    | False      | True           | ()                                                                                                                    | True         |
|   78 | @=                                    | False      | True           | ()                                                                                                                    | True         |
|   79 | //=                                   | False      | True           | ()                                                                                                                    | True         |
|   80 | %=                                    | False      | True           | ()                                                                                                                    | True         |
|   81 | \*\*=                                 | False      | True           | ()                                                                                                                    | True         |
|   82 | &gt;&gt;=                             | False      | True           | ()                                                                                                                    | True         |
|   83 | &lt;&lt;=                             | False      | True           | ()                                                                                                                    | True         |
|   84 | &amp;=                                | False      | True           | ()                                                                                                                    | True         |
|   85 | ^=                                    | False      | True           | ()                                                                                                                    | True         |
|   86 | &#124;=                               | False      | True           | ()                                                                                                                    | True         |
|   87 | yield                                 | False      | True           | ()                                                                                                                    | True         |
|   88 | ellipsis                              | True       | True           | ()                                                                                                                    | True         |
|   89 | escape\_sequence                      | True       | True           | ()                                                                                                                    | True         |
|   90 | \                                     | False      | True           | ()                                                                                                                    | True         |
|   91 | format\_specifier\_token1             | False      | False          | ()                                                                                                                    | False        |
|   92 | type\_conversion                      | True       | True           | ()                                                                                                                    | True         |
|   93 | integer                               | True       | True           | ()                                                                                                                    | True         |
|   94 | float                                 | True       | True           | ()                                                                                                                    | True         |
|   95 | await                                 | False      | True           | ()                                                                                                                    | True         |
|   96 | true                                  | True       | True           | ()                                                                                                                    | True         |
|   97 | false                                 | True       | True           | ()                                                                                                                    | True         |
|   98 | none                                  | True       | True           | ()                                                                                                                    | True         |
|   99 | comment                               | True       | True           | ()                                                                                                                    | True         |
|  100 | line\_continuation                    | True       | True           | ()                                                                                                                    | True         |
|  101 | \_newline                             | False      | False          | ()                                                                                                                    | False        |
|  102 | \_indent                              | False      | False          | ()                                                                                                                    | False        |
|  103 | \_dedent                              | False      | False          | ()                                                                                                                    | False        |
|  104 | string\_start                         | True       | True           | ()                                                                                                                    | True         |
|  105 | \_string\_content                     | False      | False          | ()                                                                                                                    | False        |
|  106 | escape\_interpolation                 | True       | True           | ()                                                                                                                    | True         |
|  107 | string\_end                           | True       | True           | ()                                                                                                                    | True         |
|  108 | module                                | True       | True           | ()                                                                                                                    | True         |
|  109 | \_statement                           | False      | False          | ()                                                                                                                    | False        |
|  110 | \_simple\_statements                  | False      | False          | ()                                                                                                                    | False        |
|  111 | import\_statement                     | True       | True           | ()                                                                                                                    | True         |
|  112 | import\_prefix                        | True       | True           | ()                                                                                                                    | True         |
|  113 | relative\_import                      | True       | True           | ()                                                                                                                    | True         |
|  114 | future\_import\_statement             | True       | True           | ()                                                                                                                    | True         |
|  115 | import\_from\_statement               | True       | True           | ()                                                                                                                    | True         |
|  116 | \_import\_list                        | False      | False          | ()                                                                                                                    | False        |
|  117 | aliased\_import                       | True       | True           | ()                                                                                                                    | True         |
|  118 | wildcard\_import                      | True       | True           | ()                                                                                                                    | True         |
|  119 | print\_statement                      | True       | True           | ()                                                                                                                    | True         |
|  120 | chevron                               | True       | True           | ()                                                                                                                    | True         |
|  121 | assert\_statement                     | True       | True           | ()                                                                                                                    | True         |
|  122 | expression\_statement                 | True       | True           | ()                                                                                                                    | True         |
|  123 | named\_expression                     | True       | True           | ()                                                                                                                    | True         |
|  124 | \_named\_expression\_lhs              | False      | False          | ()                                                                                                                    | False        |
|  125 | return\_statement                     | True       | True           | ()                                                                                                                    | True         |
|  126 | delete\_statement                     | True       | True           | ()                                                                                                                    | True         |
|  127 | raise\_statement                      | True       | True           | ()                                                                                                                    | True         |
|  128 | pass\_statement                       | True       | True           | ()                                                                                                                    | True         |
|  129 | break\_statement                      | True       | True           | ()                                                                                                                    | True         |
|  130 | continue\_statement                   | True       | True           | ()                                                                                                                    | True         |
|  131 | if\_statement                         | True       | True           | ()                                                                                                                    | True         |
|  132 | elif\_clause                          | True       | True           | ()                                                                                                                    | True         |
|  133 | else\_clause                          | True       | True           | ()                                                                                                                    | True         |
|  134 | match\_statement                      | True       | True           | ()                                                                                                                    | True         |
|  135 | block                                 | True       | True           | ()                                                                                                                    | True         |
|  136 | case\_clause                          | True       | True           | ()                                                                                                                    | True         |
|  137 | for\_statement                        | True       | True           | ()                                                                                                                    | True         |
|  138 | while\_statement                      | True       | True           | ()                                                                                                                    | True         |
|  139 | try\_statement                        | True       | True           | ()                                                                                                                    | True         |
|  140 | except\_clause                        | True       | True           | ()                                                                                                                    | True         |
|  141 | finally\_clause                       | True       | True           | ()                                                                                                                    | True         |
|  142 | with\_statement                       | True       | True           | ()                                                                                                                    | True         |
|  143 | with\_clause                          | True       | True           | ()                                                                                                                    | True         |
|  144 | with\_item                            | True       | True           | ()                                                                                                                    | True         |
|  145 | function\_definition                  | True       | True           | ()                                                                                                                    | True         |
|  146 | parameters                            | True       | True           | ()                                                                                                                    | True         |
|  147 | lambda\_parameters                    | True       | True           | ()                                                                                                                    | True         |
|  148 | list\_splat                           | True       | True           | ()                                                                                                                    | True         |
|  149 | dictionary\_splat                     | True       | True           | ()                                                                                                                    | True         |
|  150 | global\_statement                     | True       | True           | ()                                                                                                                    | True         |
|  151 | nonlocal\_statement                   | True       | True           | ()                                                                                                                    | True         |
|  152 | exec\_statement                       | True       | True           | ()                                                                                                                    | True         |
|  153 | type\_alias\_statement                | True       | True           | ()                                                                                                                    | True         |
|  154 | class\_definition                     | True       | True           | ()                                                                                                                    | True         |
|  155 | type\_parameter                       | True       | True           | ()                                                                                                                    | True         |
|  156 | parenthesized\_list\_splat            | True       | True           | ()                                                                                                                    | True         |
|  157 | argument\_list                        | True       | True           | ()                                                                                                                    | True         |
|  158 | decorated\_definition                 | True       | True           | ()                                                                                                                    | True         |
|  159 | decorator                             | True       | True           | ()                                                                                                                    | True         |
|  160 | block                                 | True       | True           | ()                                                                                                                    | True         |
|  161 | expression\_list                      | True       | True           | ()                                                                                                                    | True         |
|  162 | dotted\_name                          | True       | True           | ()                                                                                                                    | True         |
|  163 | case\_pattern                         | True       | True           | ()                                                                                                                    | True         |
|  164 | \_simple\_pattern                     | False      | False          | ()                                                                                                                    | False        |
|  165 | as\_pattern                           | True       | True           | ()                                                                                                                    | True         |
|  166 | union\_pattern                        | True       | True           | ()                                                                                                                    | True         |
|  167 | list\_pattern                         | True       | True           | ()                                                                                                                    | True         |
|  168 | tuple\_pattern                        | True       | True           | ()                                                                                                                    | True         |
|  169 | dict\_pattern                         | True       | True           | ()                                                                                                                    | True         |
|  170 | \_key\_value\_pattern                 | False      | False          | ()                                                                                                                    | False        |
|  171 | keyword\_pattern                      | True       | True           | ()                                                                                                                    | True         |
|  172 | splat\_pattern                        | True       | True           | ()                                                                                                                    | True         |
|  173 | class\_pattern                        | True       | True           | ()                                                                                                                    | True         |
|  174 | complex\_pattern                      | True       | True           | ()                                                                                                                    | True         |
|  175 | \_parameters                          | False      | False          | ()                                                                                                                    | False        |
|  176 | \_patterns                            | False      | False          | ()                                                                                                                    | False        |
|  177 | parameter                             | False      | True           | (181, 184, 1, 239, 183, 238, 179, 182, 207)                                                                           | False        |
|  178 | pattern                               | False      | True           | (203, 1, 180, 183, 204, 179)                                                                                          | False        |
|  179 | tuple\_pattern                        | True       | True           | ()                                                                                                                    | True         |
|  180 | list\_pattern                         | True       | True           | ()                                                                                                                    | True         |
|  181 | default\_parameter                    | True       | True           | ()                                                                                                                    | True         |
|  182 | typed\_default\_parameter             | True       | True           | ()                                                                                                                    | True         |
|  183 | list\_splat\_pattern                  | True       | True           | ()                                                                                                                    | True         |
|  184 | dictionary\_splat\_pattern            | True       | True           | ()                                                                                                                    | True         |
|  185 | as\_pattern                           | True       | True           | ()                                                                                                                    | True         |
|  186 | \_expression\_within\_for\_in\_clause | False      | False          | ()                                                                                                                    | False        |
|  187 | expression                            | False      | True           | (185, 190, 195, 229, 196, 123, 189, 188)                                                                              | False        |
|  188 | primary\_expression                   | False      | True           | (203, 237, 191, 206, 230, 218, 221, 88, 97, 94, 223, 1, 93, 215, 220, 148, 98, 225, 216, 222, 231, 204, 96, 217, 192) | False        |
|  189 | not\_operator                         | True       | True           | ()                                                                                                                    | True         |
|  190 | boolean\_operator                     | True       | True           | ()                                                                                                                    | True         |
|  191 | binary\_operator                      | True       | True           | ()                                                                                                                    | True         |
|  192 | unary\_operator                       | True       | True           | ()                                                                                                                    | True         |
|  193 | not in                                | False      | True           | ()                                                                                                                    | True         |
|  194 | is not                                | False      | True           | ()                                                                                                                    | True         |
|  195 | comparison\_operator                  | True       | True           | ()                                                                                                                    | True         |
|  196 | lambda                                | True       | True           | ()                                                                                                                    | True         |
|  197 | lambda                                | True       | True           | ()                                                                                                                    | True         |
|  198 | assignment                            | True       | True           | ()                                                                                                                    | True         |
|  199 | augmented\_assignment                 | True       | True           | ()                                                                                                                    | True         |
|  200 | pattern\_list                         | True       | True           | ()                                                                                                                    | True         |
|  201 | \_right\_hand\_side                   | False      | False          | ()                                                                                                                    | False        |
|  202 | yield                                 | True       | True           | ()                                                                                                                    | True         |
|  203 | attribute                             | True       | True           | ()                                                                                                                    | True         |
|  204 | subscript                             | True       | True           | ()                                                                                                                    | True         |
|  205 | slice                                 | True       | True           | ()                                                                                                                    | True         |
|  206 | call                                  | True       | True           | ()                                                                                                                    | True         |
|  207 | typed\_parameter                      | True       | True           | ()                                                                                                                    | True         |
|  208 | type                                  | True       | True           | ()                                                                                                                    | True         |
|  209 | splat\_type                           | True       | True           | ()                                                                                                                    | True         |
|  210 | generic\_type                         | True       | True           | ()                                                                                                                    | True         |
|  211 | union\_type                           | True       | True           | ()                                                                                                                    | True         |
|  212 | constrained\_type                     | True       | True           | ()                                                                                                                    | True         |
|  213 | member\_type                          | True       | True           | ()                                                                                                                    | True         |
|  214 | keyword\_argument                     | True       | True           | ()                                                                                                                    | True         |
|  215 | list                                  | True       | True           | ()                                                                                                                    | True         |
|  216 | set                                   | True       | True           | ()                                                                                                                    | True         |
|  217 | tuple                                 | True       | True           | ()                                                                                                                    | True         |
|  218 | dictionary                            | True       | True           | ()                                                                                                                    | True         |
|  219 | pair                                  | True       | True           | ()                                                                                                                    | True         |
|  220 | list\_comprehension                   | True       | True           | ()                                                                                                                    | True         |
|  221 | dictionary\_comprehension             | True       | True           | ()                                                                                                                    | True         |
|  222 | set\_comprehension                    | True       | True           | ()                                                                                                                    | True         |
|  223 | generator\_expression                 | True       | True           | ()                                                                                                                    | True         |
|  224 | \_comprehension\_clauses              | False      | False          | ()                                                                                                                    | False        |
|  225 | parenthesized\_expression             | True       | True           | ()                                                                                                                    | True         |
|  226 | \_collection\_elements                | False      | False          | ()                                                                                                                    | False        |
|  227 | for\_in\_clause                       | True       | True           | ()                                                                                                                    | True         |
|  228 | if\_clause                            | True       | True           | ()                                                                                                                    | True         |
|  229 | conditional\_expression               | True       | True           | ()                                                                                                                    | True         |
|  230 | concatenated\_string                  | True       | True           | ()                                                                                                                    | True         |
|  231 | string                                | True       | True           | ()                                                                                                                    | True         |
|  232 | string\_content                       | True       | True           | ()                                                                                                                    | True         |
|  233 | interpolation                         | True       | True           | ()                                                                                                                    | True         |
|  234 | \_f\_expression                       | False      | False          | ()                                                                                                                    | False        |
|  235 | \_not\_escape\_sequence               | False      | False          | ()                                                                                                                    | False        |
|  236 | format\_specifier                     | True       | True           | ()                                                                                                                    | True         |
|  237 | await                                 | True       | True           | ()                                                                                                                    | True         |
|  238 | positional\_separator                 | True       | True           | ()                                                                                                                    | True         |
|  239 | keyword\_separator                    | True       | True           | ()                                                                                                                    | True         |
|  240 | module\_repeat1                       | False      | False          | ()                                                                                                                    | False        |
|  241 | \_simple\_statements\_repeat1         | False      | False          | ()                                                                                                                    | False        |
|  242 | import\_prefix\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  243 | \_import\_list\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  244 | print\_statement\_repeat1             | False      | False          | ()                                                                                                                    | False        |
|  245 | assert\_statement\_repeat1            | False      | False          | ()                                                                                                                    | False        |
|  246 | if\_statement\_repeat1                | False      | False          | ()                                                                                                                    | False        |
|  247 | match\_statement\_repeat1             | False      | False          | ()                                                                                                                    | False        |
|  248 | \_match\_block\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  249 | case\_clause\_repeat1                 | False      | False          | ()                                                                                                                    | False        |
|  250 | try\_statement\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  251 | except\_clause\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  252 | with\_clause\_repeat1                 | False      | False          | ()                                                                                                                    | False        |
|  253 | global\_statement\_repeat1            | False      | False          | ()                                                                                                                    | False        |
|  254 | type\_parameter\_repeat1              | False      | False          | ()                                                                                                                    | False        |
|  255 | argument\_list\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  256 | decorated\_definition\_repeat1        | False      | False          | ()                                                                                                                    | False        |
|  257 | dotted\_name\_repeat1                 | False      | False          | ()                                                                                                                    | False        |
|  258 | union\_pattern\_repeat1               | False      | False          | ()                                                                                                                    | False        |
|  259 | dict\_pattern\_repeat1                | False      | False          | ()                                                                                                                    | False        |
|  260 | \_parameters\_repeat1                 | False      | False          | ()                                                                                                                    | False        |
|  261 | \_patterns\_repeat1                   | False      | False          | ()                                                                                                                    | False        |
|  262 | comparison\_operator\_repeat1         | False      | False          | ()                                                                                                                    | False        |
|  263 | subscript\_repeat1                    | False      | False          | ()                                                                                                                    | False        |
|  264 | dictionary\_repeat1                   | False      | False          | ()                                                                                                                    | False        |
|  265 | \_comprehension\_clauses\_repeat1     | False      | False          | ()                                                                                                                    | False        |
|  266 | \_collection\_elements\_repeat1       | False      | False          | ()                                                                                                                    | False        |
|  267 | for\_in\_clause\_repeat1              | False      | False          | ()                                                                                                                    | False        |
|  268 | concatenated\_string\_repeat1         | False      | False          | ()                                                                                                                    | False        |
|  269 | string\_repeat1                       | False      | False          | ()                                                                                                                    | False        |
|  270 | string\_content\_repeat1              | False      | False          | ()                                                                                                                    | False        |
|  271 | format\_specifier\_repeat1            | False      | False          | ()                                                                                                                    | False        |
|  272 | as\_pattern\_target                   | True       | True           | ()                                                                                                                    | True         |
|  273 | format\_expression                    | True       | True           | ()                                                                                                                    | True         |

## Fields

|   id | name              |
|------|-------------------|
|    0 | `None`            |
|    1 | alias             |
|    2 | alternative       |
|    3 | argument          |
|    4 | arguments         |
|    5 | attribute         |
|    6 | body              |
|    7 | cause             |
|    8 | code              |
|    9 | condition         |
|   10 | consequence       |
|   11 | definition        |
|   12 | expression        |
|   13 | format\_specifier |
|   14 | function          |
|   15 | guard             |
|   16 | key               |
|   17 | left              |
|   18 | module\_name      |
|   19 | name              |
|   20 | object            |
|   21 | operator          |
|   22 | operators         |
|   23 | parameters        |
|   24 | return\_type      |
|   25 | right             |
|   26 | subject           |
|   27 | subscript         |
|   28 | superclasses      |
|   29 | type              |
|   30 | type\_conversion  |
|   31 | type\_parameters  |


# RUST

- Language: rust
- ABI version: 15
- File name extensions: ['.rs']
- File name patterns: []
- Node kinds count: 355
    - Anonymous node count: 170
    - Visible node count: 300
    - Supertype node count: 305
- Field count: 31

## Node kinds

|   id | name                                       | is_named   | is_supertype   | subtype_ids                                                                                                                                                                                            | is_visible   |
|------|--------------------------------------------|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
|    0 | end                                        | False      | False          | ()                                                                                                                                                                                                     | False        |
|    1 | identifier                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|    2 | ;                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|    3 | macro\_rules!                              | False      | True           | ()                                                                                                                                                                                                     | True         |
|    4 | (                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|    5 | )                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|    6 | [                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|    7 | ]                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|    8 | {                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|    9 | }                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   10 | =&gt;                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   11 | :                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   12 | $                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   13 | token\_repetition\_pattern\_token1         | False      | False          | ()                                                                                                                                                                                                     | False        |
|   14 | +                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   15 | \*                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   16 | ?                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   17 | block                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   18 | expr                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   19 | expr\_2021                                 | False      | True           | ()                                                                                                                                                                                                     | True         |
|   20 | ident                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   21 | item                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   22 | lifetime                                   | False      | True           | ()                                                                                                                                                                                                     | True         |
|   23 | literal                                    | False      | True           | ()                                                                                                                                                                                                     | True         |
|   24 | meta                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   25 | pat                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   26 | pat\_param                                 | False      | True           | ()                                                                                                                                                                                                     | True         |
|   27 | path                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   28 | stmt                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   29 | tt                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   30 | ty                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   31 | vis                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   32 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   33 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   34 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   35 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   36 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   37 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   38 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   39 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   40 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   41 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   42 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   43 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   44 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   45 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   46 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   47 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   48 | primitive\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|   49 | -                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   50 | /                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   51 | %                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   52 | ^                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   53 | !                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   54 | &amp;                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   55 | &#124;                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|   56 | &amp;&amp;                                 | False      | True           | ()                                                                                                                                                                                                     | True         |
|   57 | &#124;&#124;                               | False      | True           | ()                                                                                                                                                                                                     | True         |
|   58 | &lt;&lt;                                   | False      | True           | ()                                                                                                                                                                                                     | True         |
|   59 | &gt;&gt;                                   | False      | True           | ()                                                                                                                                                                                                     | True         |
|   60 | +=                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   61 | -=                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   62 | \*=                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   63 | /=                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   64 | %=                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   65 | ^=                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   66 | &amp;=                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|   67 | &#124;=                                    | False      | True           | ()                                                                                                                                                                                                     | True         |
|   68 | &lt;&lt;=                                  | False      | True           | ()                                                                                                                                                                                                     | True         |
|   69 | &gt;&gt;=                                  | False      | True           | ()                                                                                                                                                                                                     | True         |
|   70 | =                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   71 | ==                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   72 | !=                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   73 | &gt;                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   74 | &lt;                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   75 | &gt;=                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   76 | &lt;=                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   77 | @                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   78 | \_                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   79 | .                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   80 | ..                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   81 | ...                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   82 | ..=                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   83 | ,                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   84 | ::                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   85 | -&gt;                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   86 | #                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   87 | '                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|   88 | as                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   89 | async                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   90 | await                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   91 | break                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   92 | const                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|   93 | continue                                   | False      | True           | ()                                                                                                                                                                                                     | True         |
|   94 | default                                    | False      | True           | ()                                                                                                                                                                                                     | True         |
|   95 | enum                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|   96 | fn                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|   97 | for                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   98 | gen                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|   99 | if                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|  100 | impl                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  101 | let                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  102 | loop                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  103 | match                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  104 | mod                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  105 | pub                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  106 | return                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|  107 | static                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|  108 | struct                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|  109 | trait                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  110 | type                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  111 | union                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  112 | unsafe                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|  113 | use                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  114 | where                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  115 | while                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  116 | extern                                     | False      | True           | ()                                                                                                                                                                                                     | True         |
|  117 | ref                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  118 | else                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  119 | in                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|  120 | &lt;                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  121 | dyn                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  122 | mutable\_specifier                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  123 | raw                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  124 | yield                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  125 | move                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  126 | try                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  127 | integer\_literal                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  128 | "                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|  129 | char\_literal                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  130 | escape\_sequence                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  131 | true                                       | False      | True           | ()                                                                                                                                                                                                     | True         |
|  132 | false                                      | False      | True           | ()                                                                                                                                                                                                     | True         |
|  133 | //                                         | False      | True           | ()                                                                                                                                                                                                     | True         |
|  134 | line\_comment\_token1                      | False      | False          | ()                                                                                                                                                                                                     | False        |
|  135 | line\_comment\_token2                      | False      | False          | ()                                                                                                                                                                                                     | False        |
|  136 | line\_comment\_token3                      | False      | False          | ()                                                                                                                                                                                                     | False        |
|  137 | !                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|  138 | /                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|  139 | /\*                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  140 | \*/                                        | False      | True           | ()                                                                                                                                                                                                     | True         |
|  141 | shebang                                    | True       | True           | ()                                                                                                                                                                                                     | True         |
|  142 | self                                       | True       | True           | ()                                                                                                                                                                                                     | True         |
|  143 | super                                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  144 | crate                                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  145 | metavariable                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  146 | string\_content                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  147 | "                                          | False      | True           | ()                                                                                                                                                                                                     | True         |
|  148 | \_raw\_string\_literal\_start              | False      | False          | ()                                                                                                                                                                                                     | False        |
|  149 | string\_content                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  150 | \_raw\_string\_literal\_end                | False      | False          | ()                                                                                                                                                                                                     | False        |
|  151 | float\_literal                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  152 | outer\_doc\_comment\_marker                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  153 | inner\_doc\_comment\_marker                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  154 | \_block\_comment\_content                  | False      | False          | ()                                                                                                                                                                                                     | False        |
|  155 | doc\_comment                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  156 | \_error\_sentinel                          | False      | False          | ()                                                                                                                                                                                                     | False        |
|  157 | source\_file                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  158 | \_statement                                | False      | False          | ()                                                                                                                                                                                                     | False        |
|  159 | empty\_statement                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  160 | expression\_statement                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  161 | macro\_definition                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  162 | macro\_rule                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  163 | \_token\_pattern                           | False      | False          | ()                                                                                                                                                                                                     | False        |
|  164 | token\_tree\_pattern                       | True       | True           | ()                                                                                                                                                                                                     | True         |
|  165 | token\_binding\_pattern                    | True       | True           | ()                                                                                                                                                                                                     | True         |
|  166 | token\_repetition\_pattern                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  167 | fragment\_specifier                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  168 | token\_tree                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  169 | token\_repetition                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  170 | attribute\_item                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  171 | inner\_attribute\_item                     | True       | True           | ()                                                                                                                                                                                                     | True         |
|  172 | attribute                                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  173 | mod\_item                                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  174 | foreign\_mod\_item                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  175 | declaration\_list                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  176 | struct\_item                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  177 | union\_item                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  178 | enum\_item                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  179 | enum\_variant\_list                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  180 | enum\_variant                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  181 | field\_declaration\_list                   | True       | True           | ()                                                                                                                                                                                                     | True         |
|  182 | field\_declaration                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  183 | ordered\_field\_declaration\_list          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  184 | extern\_crate\_declaration                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  185 | const\_item                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  186 | static\_item                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  187 | type\_item                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  188 | function\_item                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  189 | function\_signature\_item                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  190 | function\_modifiers                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  191 | where\_clause                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  192 | where\_predicate                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  193 | impl\_item                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  194 | trait\_item                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  195 | associated\_type                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  196 | trait\_bounds                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  197 | higher\_ranked\_trait\_bound               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  198 | removed\_trait\_bound                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  199 | type\_parameters                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  200 | const\_parameter                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  201 | type\_parameter                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  202 | lifetime\_parameter                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  203 | let\_declaration                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  204 | use\_declaration                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  205 | \_use\_clause                              | False      | False          | ()                                                                                                                                                                                                     | False        |
|  206 | scoped\_use\_list                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  207 | use\_list                                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  208 | use\_as\_clause                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  209 | use\_wildcard                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  210 | parameters                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  211 | self\_parameter                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  212 | variadic\_parameter                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  213 | parameter                                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  214 | extern\_modifier                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  215 | visibility\_modifier                       | True       | True           | ()                                                                                                                                                                                                     | True         |
|  216 | \_type                                     | False      | True           | (354, 46, 48, 44, 45, 41, 35, 37, 39, 33, 42, 47, 40, 34, 36, 38, 32, 43, 235, 220, 228, 236, 222, 226, 239, 145, 234, 233, 232, 198, 245, 223, 224)                                                   | False        |
|  217 | bracketed\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  218 | qualified\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  219 | lifetime                                   | True       | True           | ()                                                                                                                                                                                                     | True         |
|  220 | array\_type                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  221 | for\_lifetimes                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  222 | function\_type                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  223 | tuple\_type                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  224 | unit\_type                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  225 | generic\_function                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  226 | generic\_type                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  227 | generic\_type\_with\_turbofish             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  228 | bounded\_type                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  229 | use\_bounds                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  230 | type\_arguments                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  231 | type\_binding                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  232 | reference\_type                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  233 | pointer\_type                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  234 | never\_type                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  235 | abstract\_type                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  236 | dynamic\_type                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  237 | \_expression\_except\_range                | False      | False          | ()                                                                                                                                                                                                     | False        |
|  238 | \_expression                               | False      | True           | (308, 258, 251, 290, 287, 250, 293, 284, 256, 281, 252, 280, 285, 288, 279, 291, 225, 1, 267, 286, 278, 239, 272, 145, 259, 246, 249, 254, 243, 142, 262, 292, 248, 260, 253, 247, 261, 289, 277, 255) | False        |
|  239 | macro\_invocation                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  240 | token\_tree                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  241 | \_delim\_tokens                            | False      | False          | ()                                                                                                                                                                                                     | False        |
|  242 | \_non\_delim\_token                        | False      | False          | ()                                                                                                                                                                                                     | False        |
|  243 | scoped\_identifier                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  244 | scoped\_type\_identifier                   | True       | True           | ()                                                                                                                                                                                                     | True         |
|  245 | scoped\_type\_identifier                   | True       | True           | ()                                                                                                                                                                                                     | True         |
|  246 | range\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  247 | unary\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  248 | try\_expression                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  249 | reference\_expression                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  250 | binary\_expression                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  251 | assignment\_expression                     | True       | True           | ()                                                                                                                                                                                                     | True         |
|  252 | compound\_assignment\_expr                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  253 | type\_cast\_expression                     | True       | True           | ()                                                                                                                                                                                                     | True         |
|  254 | return\_expression                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  255 | yield\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  256 | call\_expression                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  257 | arguments                                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  258 | array\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  259 | parenthesized\_expression                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  260 | tuple\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  261 | unit\_expression                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  262 | struct\_expression                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  263 | field\_initializer\_list                   | True       | True           | ()                                                                                                                                                                                                     | True         |
|  264 | shorthand\_field\_initializer              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  265 | field\_initializer                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  266 | base\_field\_initializer                   | True       | True           | ()                                                                                                                                                                                                     | True         |
|  267 | if\_expression                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  268 | let\_condition                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  269 | \_let\_chain                               | False      | False          | ()                                                                                                                                                                                                     | False        |
|  270 | \_condition                                | False      | False          | ()                                                                                                                                                                                                     | False        |
|  271 | else\_clause                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  272 | match\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  273 | match\_block                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  274 | match\_arm                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  275 | match\_arm                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  276 | match\_pattern                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  277 | while\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  278 | loop\_expression                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  279 | for\_expression                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  280 | const\_block                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  281 | closure\_expression                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  282 | closure\_parameters                        | True       | True           | ()                                                                                                                                                                                                     | True         |
|  283 | label                                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  284 | break\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  285 | continue\_expression                       | True       | True           | ()                                                                                                                                                                                                     | True         |
|  286 | index\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  287 | await\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  288 | field\_expression                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  289 | unsafe\_block                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  290 | async\_block                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  291 | gen\_block                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  292 | try\_block                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  293 | block                                      | True       | True           | ()                                                                                                                                                                                                     | True         |
|  294 | \_pattern                                  | False      | True           | (78, 309, 305, 280, 295, 1, 239, 302, 307, 303, 304, 306, 301, 243, 297, 299, 296, 298)                                                                                                                | False        |
|  295 | generic\_pattern                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  296 | tuple\_pattern                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  297 | slice\_pattern                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  298 | tuple\_struct\_pattern                     | True       | True           | ()                                                                                                                                                                                                     | True         |
|  299 | struct\_pattern                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  300 | field\_pattern                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  301 | remaining\_field\_pattern                  | True       | True           | ()                                                                                                                                                                                                     | True         |
|  302 | mut\_pattern                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  303 | range\_pattern                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  304 | ref\_pattern                               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  305 | captured\_pattern                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  306 | reference\_pattern                         | True       | True           | ()                                                                                                                                                                                                     | True         |
|  307 | or\_pattern                                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  308 | \_literal                                  | False      | True           | (313, 129, 151, 127, 312, 311)                                                                                                                                                                         | False        |
|  309 | \_literal\_pattern                         | False      | True           | (313, 129, 151, 127, 310, 312, 311)                                                                                                                                                                    | False        |
|  310 | negative\_literal                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  311 | string\_literal                            | True       | True           | ()                                                                                                                                                                                                     | True         |
|  312 | raw\_string\_literal                       | True       | True           | ()                                                                                                                                                                                                     | True         |
|  313 | boolean\_literal                           | True       | True           | ()                                                                                                                                                                                                     | True         |
|  314 | line\_comment                              | True       | True           | ()                                                                                                                                                                                                     | True         |
|  315 | \_line\_doc\_comment\_marker               | False      | False          | ()                                                                                                                                                                                                     | False        |
|  316 | inner\_doc\_comment\_marker                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  317 | outer\_doc\_comment\_marker                | True       | True           | ()                                                                                                                                                                                                     | True         |
|  318 | block\_comment                             | True       | True           | ()                                                                                                                                                                                                     | True         |
|  319 | \_block\_doc\_comment\_marker              | False      | False          | ()                                                                                                                                                                                                     | False        |
|  320 | source\_file\_repeat1                      | False      | False          | ()                                                                                                                                                                                                     | False        |
|  321 | macro\_definition\_repeat1                 | False      | False          | ()                                                                                                                                                                                                     | False        |
|  322 | token\_tree\_pattern\_repeat1              | False      | False          | ()                                                                                                                                                                                                     | False        |
|  323 | token\_tree\_repeat1                       | False      | False          | ()                                                                                                                                                                                                     | False        |
|  324 | \_non\_special\_token\_repeat1             | False      | False          | ()                                                                                                                                                                                                     | False        |
|  325 | declaration\_list\_repeat1                 | False      | False          | ()                                                                                                                                                                                                     | False        |
|  326 | enum\_variant\_list\_repeat1               | False      | False          | ()                                                                                                                                                                                                     | False        |
|  327 | enum\_variant\_list\_repeat2               | False      | False          | ()                                                                                                                                                                                                     | False        |
|  328 | field\_declaration\_list\_repeat1          | False      | False          | ()                                                                                                                                                                                                     | False        |
|  329 | ordered\_field\_declaration\_list\_repeat1 | False      | False          | ()                                                                                                                                                                                                     | False        |
|  330 | function\_modifiers\_repeat1               | False      | False          | ()                                                                                                                                                                                                     | False        |
|  331 | where\_clause\_repeat1                     | False      | False          | ()                                                                                                                                                                                                     | False        |
|  332 | trait\_bounds\_repeat1                     | False      | False          | ()                                                                                                                                                                                                     | False        |
|  333 | type\_parameters\_repeat1                  | False      | False          | ()                                                                                                                                                                                                     | False        |
|  334 | use\_list\_repeat1                         | False      | False          | ()                                                                                                                                                                                                     | False        |
|  335 | parameters\_repeat1                        | False      | False          | ()                                                                                                                                                                                                     | False        |
|  336 | for\_lifetimes\_repeat1                    | False      | False          | ()                                                                                                                                                                                                     | False        |
|  337 | tuple\_type\_repeat1                       | False      | False          | ()                                                                                                                                                                                                     | False        |
|  338 | use\_bounds\_repeat1                       | False      | False          | ()                                                                                                                                                                                                     | False        |
|  339 | type\_arguments\_repeat1                   | False      | False          | ()                                                                                                                                                                                                     | False        |
|  340 | delim\_token\_tree\_repeat1                | False      | False          | ()                                                                                                                                                                                                     | False        |
|  341 | arguments\_repeat1                         | False      | False          | ()                                                                                                                                                                                                     | False        |
|  342 | tuple\_expression\_repeat1                 | False      | False          | ()                                                                                                                                                                                                     | False        |
|  343 | field\_initializer\_list\_repeat1          | False      | False          | ()                                                                                                                                                                                                     | False        |
|  344 | match\_block\_repeat1                      | False      | False          | ()                                                                                                                                                                                                     | False        |
|  345 | match\_arm\_repeat1                        | False      | False          | ()                                                                                                                                                                                                     | False        |
|  346 | closure\_parameters\_repeat1               | False      | False          | ()                                                                                                                                                                                                     | False        |
|  347 | tuple\_pattern\_repeat1                    | False      | False          | ()                                                                                                                                                                                                     | False        |
|  348 | slice\_pattern\_repeat1                    | False      | False          | ()                                                                                                                                                                                                     | False        |
|  349 | struct\_pattern\_repeat1                   | False      | False          | ()                                                                                                                                                                                                     | False        |
|  350 | string\_literal\_repeat1                   | False      | False          | ()                                                                                                                                                                                                     | False        |
|  351 | field\_identifier                          | True       | True           | ()                                                                                                                                                                                                     | True         |
|  352 | let\_chain                                 | True       | True           | ()                                                                                                                                                                                                     | True         |
|  353 | shorthand\_field\_identifier               | True       | True           | ()                                                                                                                                                                                                     | True         |
|  354 | type\_identifier                           | True       | True           | ()                                                                                                                                                                                                     | True         |

## Fields

|   id | name             |
|------|------------------|
|    0 | `None`           |
|    1 | alias            |
|    2 | alternative      |
|    3 | argument         |
|    4 | arguments        |
|    5 | body             |
|    6 | bounds           |
|    7 | condition        |
|    8 | consequence      |
|    9 | default\_type    |
|   10 | doc              |
|   11 | element          |
|   12 | field            |
|   13 | function         |
|   14 | inner            |
|   15 | left             |
|   16 | length           |
|   17 | list             |
|   18 | macro            |
|   19 | name             |
|   20 | operator         |
|   21 | outer            |
|   22 | parameters       |
|   23 | path             |
|   24 | pattern          |
|   25 | return\_type     |
|   26 | right            |
|   27 | trait            |
|   28 | type             |
|   29 | type\_arguments  |
|   30 | type\_parameters |


# TOML

- Language: toml
- ABI version: 14
- File name extensions: ['.toml']
- File name patterns: []
- Node kinds count: 66
    - Anonymous node count: 46
    - Visible node count: 35
    - Supertype node count: 35
- Field count: 0

## Node kinds

|   id | name                                  | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|---------------------------------------|------------|----------------|---------------|--------------|
|    0 | end                                   | False      | False          | ()            | False        |
|    1 | document\_token1                      | False      | False          | ()            | False        |
|    2 | comment                               | True       | True           | ()            | True         |
|    3 | [                                     | False      | True           | ()            | True         |
|    4 | ]                                     | False      | True           | ()            | True         |
|    5 | [[                                    | False      | True           | ()            | True         |
|    6 | ]]                                    | False      | True           | ()            | True         |
|    7 | =                                     | False      | True           | ()            | True         |
|    8 | .                                     | False      | True           | ()            | True         |
|    9 | bare\_key                             | True       | True           | ()            | True         |
|   10 | "                                     | False      | True           | ()            | True         |
|   11 | \_basic\_string\_token1               | False      | False          | ()            | False        |
|   12 | "                                     | False      | True           | ()            | True         |
|   13 | """                                   | False      | True           | ()            | True         |
|   14 | \_multiline\_basic\_string\_token1    | False      | False          | ()            | False        |
|   15 | escape\_sequence                      | True       | True           | ()            | True         |
|   16 | escape\_sequence                      | True       | True           | ()            | True         |
|   17 | '                                     | False      | True           | ()            | True         |
|   18 | \_literal\_string\_token1             | False      | False          | ()            | False        |
|   19 | '                                     | False      | True           | ()            | True         |
|   20 | '''                                   | False      | True           | ()            | True         |
|   21 | integer\_token1                       | False      | False          | ()            | False        |
|   22 | integer\_token2                       | False      | False          | ()            | False        |
|   23 | integer\_token3                       | False      | False          | ()            | False        |
|   24 | integer\_token4                       | False      | False          | ()            | False        |
|   25 | float\_token1                         | False      | False          | ()            | False        |
|   26 | float\_token2                         | False      | False          | ()            | False        |
|   27 | boolean                               | True       | True           | ()            | True         |
|   28 | offset\_date\_time                    | True       | True           | ()            | True         |
|   29 | local\_date\_time                     | True       | True           | ()            | True         |
|   30 | local\_date                           | True       | True           | ()            | True         |
|   31 | local\_time                           | True       | True           | ()            | True         |
|   32 | ,                                     | False      | True           | ()            | True         |
|   33 | {                                     | False      | True           | ()            | True         |
|   34 | }                                     | False      | True           | ()            | True         |
|   35 | \_line\_ending\_or\_eof               | False      | False          | ()            | False        |
|   36 | \_multiline\_basic\_string\_content   | False      | False          | ()            | False        |
|   37 | \_multiline\_basic\_string\_end       | False      | False          | ()            | False        |
|   38 | \_multiline\_literal\_string\_content | False      | False          | ()            | False        |
|   39 | \_multiline\_literal\_string\_end     | False      | False          | ()            | False        |
|   40 | document                              | True       | True           | ()            | True         |
|   41 | table                                 | True       | True           | ()            | True         |
|   42 | table\_array\_element                 | True       | True           | ()            | True         |
|   43 | pair                                  | True       | True           | ()            | True         |
|   44 | \_inline\_pair                        | False      | False          | ()            | False        |
|   45 | \_key                                 | False      | False          | ()            | False        |
|   46 | dotted\_key                           | True       | True           | ()            | True         |
|   47 | quoted\_key                           | True       | True           | ()            | True         |
|   48 | \_inline\_value                       | False      | False          | ()            | False        |
|   49 | string                                | True       | True           | ()            | True         |
|   50 | \_basic\_string                       | False      | False          | ()            | False        |
|   51 | \_multiline\_basic\_string            | False      | False          | ()            | False        |
|   52 | \_literal\_string                     | False      | False          | ()            | False        |
|   53 | \_multiline\_literal\_string          | False      | False          | ()            | False        |
|   54 | integer                               | True       | True           | ()            | True         |
|   55 | float                                 | True       | True           | ()            | True         |
|   56 | array                                 | True       | True           | ()            | True         |
|   57 | inline\_table                         | True       | True           | ()            | True         |
|   58 | document\_repeat1                     | False      | False          | ()            | False        |
|   59 | document\_repeat2                     | False      | False          | ()            | False        |
|   60 | \_basic\_string\_repeat1              | False      | False          | ()            | False        |
|   61 | \_multiline\_basic\_string\_repeat1   | False      | False          | ()            | False        |
|   62 | \_multiline\_literal\_string\_repeat1 | False      | False          | ()            | False        |
|   63 | array\_repeat1                        | False      | False          | ()            | False        |
|   64 | array\_repeat2                        | False      | False          | ()            | False        |
|   65 | inline\_table\_repeat1                | False      | False          | ()            | False        |

## Fields




# YAML

- Language: yaml
- ABI version: 14
- File name extensions: ['.yaml', '.yml']
- File name patterns: []
- Node kinds count: 301
    - Anonymous node count: 140
    - Visible node count: 213
    - Supertype node count: 213
- Field count: 2

## Node kinds

|   id | name                             | is_named   | is_supertype   | subtype_ids   | is_visible   |
|------|----------------------------------|------------|----------------|---------------|--------------|
|    0 | end                              | False      | False          | ()            | False        |
|    1 | \_eof                            | False      | False          | ()            | False        |
|    2 | \_s\_dir\_yml\_bgn               | False      | False          | ()            | False        |
|    3 | yaml\_version                    | True       | True           | ()            | True         |
|    4 | \_s\_dir\_tag\_bgn               | False      | False          | ()            | False        |
|    5 | tag\_handle                      | True       | True           | ()            | True         |
|    6 | tag\_prefix                      | True       | True           | ()            | True         |
|    7 | directive\_name                  | True       | True           | ()            | True         |
|    8 | directive\_parameter             | True       | True           | ()            | True         |
|    9 | ---                              | False      | True           | ()            | True         |
|   10 | ...                              | False      | True           | ()            | True         |
|   11 | -                                | False      | True           | ()            | True         |
|   12 | -                                | False      | True           | ()            | True         |
|   13 | -                                | False      | True           | ()            | True         |
|   14 | ?                                | False      | True           | ()            | True         |
|   15 | ?                                | False      | True           | ()            | True         |
|   16 | ?                                | False      | True           | ()            | True         |
|   17 | :                                | False      | True           | ()            | True         |
|   18 | :                                | False      | True           | ()            | True         |
|   19 | :                                | False      | True           | ()            | True         |
|   20 | :                                | False      | True           | ()            | True         |
|   21 | &#124;                           | False      | True           | ()            | True         |
|   22 | &#124;                           | False      | True           | ()            | True         |
|   23 | &gt;                             | False      | True           | ()            | True         |
|   24 | &gt;                             | False      | True           | ()            | True         |
|   25 | \_br\_blk\_str\_ctn              | False      | False          | ()            | False        |
|   26 | [                                | False      | True           | ()            | True         |
|   27 | [                                | False      | True           | ()            | True         |
|   28 | [                                | False      | True           | ()            | True         |
|   29 | ]                                | False      | True           | ()            | True         |
|   30 | ]                                | False      | True           | ()            | True         |
|   31 | ]                                | False      | True           | ()            | True         |
|   32 | {                                | False      | True           | ()            | True         |
|   33 | {                                | False      | True           | ()            | True         |
|   34 | {                                | False      | True           | ()            | True         |
|   35 | }                                | False      | True           | ()            | True         |
|   36 | }                                | False      | True           | ()            | True         |
|   37 | }                                | False      | True           | ()            | True         |
|   38 | ,                                | False      | True           | ()            | True         |
|   39 | ,                                | False      | True           | ()            | True         |
|   40 | ?                                | False      | True           | ()            | True         |
|   41 | ?                                | False      | True           | ()            | True         |
|   42 | :                                | False      | True           | ()            | True         |
|   43 | :                                | False      | True           | ()            | True         |
|   44 | :                                | False      | True           | ()            | True         |
|   45 | :                                | False      | True           | ()            | True         |
|   46 | "                                | False      | True           | ()            | True         |
|   47 | "                                | False      | True           | ()            | True         |
|   48 | "                                | False      | True           | ()            | True         |
|   49 | \_r\_dqt\_str\_ctn               | False      | False          | ()            | False        |
|   50 | \_br\_dqt\_str\_ctn              | False      | False          | ()            | False        |
|   51 | escape\_sequence                 | True       | True           | ()            | True         |
|   52 | escape\_sequence                 | True       | True           | ()            | True         |
|   53 | escape\_sequence                 | True       | True           | ()            | True         |
|   54 | escape\_sequence                 | True       | True           | ()            | True         |
|   55 | "                                | False      | True           | ()            | True         |
|   56 | "                                | False      | True           | ()            | True         |
|   57 | '                                | False      | True           | ()            | True         |
|   58 | '                                | False      | True           | ()            | True         |
|   59 | '                                | False      | True           | ()            | True         |
|   60 | \_r\_sqt\_str\_ctn               | False      | False          | ()            | False        |
|   61 | \_br\_sqt\_str\_ctn              | False      | False          | ()            | False        |
|   62 | escape\_sequence                 | True       | True           | ()            | True         |
|   63 | escape\_sequence                 | True       | True           | ()            | True         |
|   64 | '                                | False      | True           | ()            | True         |
|   65 | '                                | False      | True           | ()            | True         |
|   66 | null\_scalar                     | True       | True           | ()            | True         |
|   67 | null\_scalar                     | True       | True           | ()            | True         |
|   68 | null\_scalar                     | True       | True           | ()            | True         |
|   69 | null\_scalar                     | True       | True           | ()            | True         |
|   70 | null\_scalar                     | True       | True           | ()            | True         |
|   71 | boolean\_scalar                  | True       | True           | ()            | True         |
|   72 | boolean\_scalar                  | True       | True           | ()            | True         |
|   73 | boolean\_scalar                  | True       | True           | ()            | True         |
|   74 | boolean\_scalar                  | True       | True           | ()            | True         |
|   75 | boolean\_scalar                  | True       | True           | ()            | True         |
|   76 | integer\_scalar                  | True       | True           | ()            | True         |
|   77 | integer\_scalar                  | True       | True           | ()            | True         |
|   78 | integer\_scalar                  | True       | True           | ()            | True         |
|   79 | integer\_scalar                  | True       | True           | ()            | True         |
|   80 | integer\_scalar                  | True       | True           | ()            | True         |
|   81 | float\_scalar                    | True       | True           | ()            | True         |
|   82 | float\_scalar                    | True       | True           | ()            | True         |
|   83 | float\_scalar                    | True       | True           | ()            | True         |
|   84 | float\_scalar                    | True       | True           | ()            | True         |
|   85 | float\_scalar                    | True       | True           | ()            | True         |
|   86 | timestamp\_scalar                | True       | True           | ()            | True         |
|   87 | timestamp\_scalar                | True       | True           | ()            | True         |
|   88 | timestamp\_scalar                | True       | True           | ()            | True         |
|   89 | timestamp\_scalar                | True       | True           | ()            | True         |
|   90 | timestamp\_scalar                | True       | True           | ()            | True         |
|   91 | string\_scalar                   | True       | True           | ()            | True         |
|   92 | string\_scalar                   | True       | True           | ()            | True         |
|   93 | string\_scalar                   | True       | True           | ()            | True         |
|   94 | string\_scalar                   | True       | True           | ()            | True         |
|   95 | string\_scalar                   | True       | True           | ()            | True         |
|   96 | string\_scalar                   | True       | True           | ()            | True         |
|   97 | string\_scalar                   | True       | True           | ()            | True         |
|   98 | string\_scalar                   | True       | True           | ()            | True         |
|   99 | string\_scalar                   | True       | True           | ()            | True         |
|  100 | tag                              | True       | True           | ()            | True         |
|  101 | tag                              | True       | True           | ()            | True         |
|  102 | tag                              | True       | True           | ()            | True         |
|  103 | &amp;                            | False      | True           | ()            | True         |
|  104 | &amp;                            | False      | True           | ()            | True         |
|  105 | &amp;                            | False      | True           | ()            | True         |
|  106 | anchor\_name                     | True       | True           | ()            | True         |
|  107 | \*                               | False      | True           | ()            | True         |
|  108 | \*                               | False      | True           | ()            | True         |
|  109 | \*                               | False      | True           | ()            | True         |
|  110 | alias\_name                      | True       | True           | ()            | True         |
|  111 | \_bl                             | False      | False          | ()            | False        |
|  112 | comment                          | True       | True           | ()            | True         |
|  113 | \_err\_rec                       | False      | False          | ()            | False        |
|  114 | stream                           | True       | True           | ()            | True         |
|  115 | \_doc\_w\_bgn\_w\_end\_seq       | False      | False          | ()            | False        |
|  116 | \_doc\_w\_bgn\_wo\_end\_seq      | False      | False          | ()            | False        |
|  117 | \_doc\_wo\_bgn\_w\_end\_seq      | False      | False          | ()            | False        |
|  118 | \_doc\_wo\_bgn\_wo\_end\_seq     | False      | False          | ()            | False        |
|  119 | \_doc\_w\_bgn\_w\_end            | False      | False          | ()            | False        |
|  120 | \_doc\_w\_bgn\_wo\_end           | False      | False          | ()            | False        |
|  121 | \_doc\_wo\_bgn\_w\_end           | False      | False          | ()            | False        |
|  122 | \_doc\_wo\_bgn\_wo\_end          | False      | False          | ()            | False        |
|  123 | \_bgn\_imp\_doc                  | False      | False          | ()            | False        |
|  124 | \_drs\_doc                       | False      | False          | ()            | False        |
|  125 | \_exp\_doc                       | False      | False          | ()            | False        |
|  126 | \_imp\_doc                       | False      | False          | ()            | False        |
|  127 | document                         | True       | True           | ()            | True         |
|  128 | document                         | True       | True           | ()            | True         |
|  129 | document                         | True       | True           | ()            | True         |
|  130 | document                         | True       | True           | ()            | True         |
|  131 | document                         | True       | True           | ()            | True         |
|  132 | \_exp\_doc\_tal                  | False      | False          | ()            | False        |
|  133 | \_s\_dir                         | False      | False          | ()            | False        |
|  134 | yaml\_directive                  | True       | True           | ()            | True         |
|  135 | tag\_directive                   | True       | True           | ()            | True         |
|  136 | reserved\_directive              | True       | True           | ()            | True         |
|  137 | flow\_node                       | True       | True           | ()            | True         |
|  138 | flow\_node                       | True       | True           | ()            | True         |
|  139 | flow\_node                       | True       | True           | ()            | True         |
|  140 | flow\_node                       | True       | True           | ()            | True         |
|  141 | flow\_node                       | True       | True           | ()            | True         |
|  142 | \_r\_prp                         | False      | False          | ()            | False        |
|  143 | \_br\_prp                        | False      | False          | ()            | False        |
|  144 | \_r\_sgl\_prp                    | False      | False          | ()            | False        |
|  145 | \_br\_sgl\_prp                   | False      | False          | ()            | False        |
|  146 | \_b\_sgl\_prp                    | False      | False          | ()            | False        |
|  147 | block\_node                      | True       | True           | ()            | True         |
|  148 | block\_node                      | True       | True           | ()            | True         |
|  149 | block\_node                      | True       | True           | ()            | True         |
|  150 | block\_node                      | True       | True           | ()            | True         |
|  151 | block\_node                      | True       | True           | ()            | True         |
|  152 | block\_node                      | True       | True           | ()            | True         |
|  153 | block\_sequence                  | True       | True           | ()            | True         |
|  154 | block\_sequence                  | True       | True           | ()            | True         |
|  155 | block\_sequence                  | True       | True           | ()            | True         |
|  156 | block\_sequence\_item            | True       | True           | ()            | True         |
|  157 | block\_sequence\_item            | True       | True           | ()            | True         |
|  158 | block\_sequence\_item            | True       | True           | ()            | True         |
|  159 | \_blk\_seq\_itm\_tal             | False      | False          | ()            | False        |
|  160 | block\_node                      | True       | True           | ()            | True         |
|  161 | block\_node                      | True       | True           | ()            | True         |
|  162 | block\_node                      | True       | True           | ()            | True         |
|  163 | block\_mapping                   | True       | True           | ()            | True         |
|  164 | block\_mapping                   | True       | True           | ()            | True         |
|  165 | \_r\_blk\_map\_itm               | False      | False          | ()            | False        |
|  166 | \_br\_blk\_map\_itm              | False      | False          | ()            | False        |
|  167 | \_b\_blk\_map\_itm               | False      | False          | ()            | False        |
|  168 | block\_mapping\_pair             | True       | True           | ()            | True         |
|  169 | block\_mapping\_pair             | True       | True           | ()            | True         |
|  170 | block\_mapping\_pair             | True       | True           | ()            | True         |
|  171 | \_r\_blk\_key\_itm               | False      | False          | ()            | False        |
|  172 | \_br\_blk\_key\_itm              | False      | False          | ()            | False        |
|  173 | \_b\_blk\_key\_itm               | False      | False          | ()            | False        |
|  174 | \_r\_blk\_val\_itm               | False      | False          | ()            | False        |
|  175 | \_br\_blk\_val\_itm              | False      | False          | ()            | False        |
|  176 | \_b\_blk\_val\_itm               | False      | False          | ()            | False        |
|  177 | block\_mapping\_pair             | True       | True           | ()            | True         |
|  178 | block\_mapping\_pair             | True       | True           | ()            | True         |
|  179 | block\_mapping\_pair             | True       | True           | ()            | True         |
|  180 | \_blk\_exp\_itm\_tal             | False      | False          | ()            | False        |
|  181 | \_blk\_imp\_itm\_tal             | False      | False          | ()            | False        |
|  182 | block\_node                      | True       | True           | ()            | True         |
|  183 | block\_node                      | True       | True           | ()            | True         |
|  184 | block\_scalar                    | True       | True           | ()            | True         |
|  185 | block\_scalar                    | True       | True           | ()            | True         |
|  186 | flow\_node                       | True       | True           | ()            | True         |
|  187 | flow\_node                       | True       | True           | ()            | True         |
|  188 | flow\_node                       | True       | True           | ()            | True         |
|  189 | flow\_node                       | True       | True           | ()            | True         |
|  190 | flow\_node                       | True       | True           | ()            | True         |
|  191 | flow\_sequence                   | True       | True           | ()            | True         |
|  192 | flow\_sequence                   | True       | True           | ()            | True         |
|  193 | flow\_sequence                   | True       | True           | ()            | True         |
|  194 | flow\_sequence                   | True       | True           | ()            | True         |
|  195 | flow\_sequence                   | True       | True           | ()            | True         |
|  196 | \_flw\_seq\_tal                  | False      | False          | ()            | False        |
|  197 | \_sgl\_flw\_seq\_tal             | False      | False          | ()            | False        |
|  198 | flow\_node                       | True       | True           | ()            | True         |
|  199 | flow\_node                       | True       | True           | ()            | True         |
|  200 | flow\_node                       | True       | True           | ()            | True         |
|  201 | flow\_node                       | True       | True           | ()            | True         |
|  202 | flow\_node                       | True       | True           | ()            | True         |
|  203 | flow\_mapping                    | True       | True           | ()            | True         |
|  204 | flow\_mapping                    | True       | True           | ()            | True         |
|  205 | flow\_mapping                    | True       | True           | ()            | True         |
|  206 | flow\_mapping                    | True       | True           | ()            | True         |
|  207 | flow\_mapping                    | True       | True           | ()            | True         |
|  208 | \_flw\_map\_tal                  | False      | False          | ()            | False        |
|  209 | \_sgl\_flw\_map\_tal             | False      | False          | ()            | False        |
|  210 | \_r\_flw\_seq\_dat               | False      | False          | ()            | False        |
|  211 | \_br\_flw\_seq\_dat              | False      | False          | ()            | False        |
|  212 | \_r\_flw\_map\_dat               | False      | False          | ()            | False        |
|  213 | \_br\_flw\_map\_dat              | False      | False          | ()            | False        |
|  214 | \_r\_sgl\_flw\_col\_dat          | False      | False          | ()            | False        |
|  215 | \_flw\_seq\_dat\_rpt             | False      | False          | ()            | False        |
|  216 | \_flw\_map\_dat\_rpt             | False      | False          | ()            | False        |
|  217 | \_sgl\_flw\_col\_dat\_rpt        | False      | False          | ()            | False        |
|  218 | \_r\_flw\_seq\_itm               | False      | False          | ()            | False        |
|  219 | \_br\_flw\_seq\_itm              | False      | False          | ()            | False        |
|  220 | \_r\_flw\_map\_itm               | False      | False          | ()            | False        |
|  221 | \_br\_flw\_map\_itm              | False      | False          | ()            | False        |
|  222 | \_r\_sgl\_flw\_col\_itm          | False      | False          | ()            | False        |
|  223 | flow\_pair                       | True       | True           | ()            | True         |
|  224 | flow\_pair                       | True       | True           | ()            | True         |
|  225 | flow\_pair                       | True       | True           | ()            | True         |
|  226 | \_r\_flw\_imp\_r\_par            | False      | False          | ()            | False        |
|  227 | \_r\_flw\_imp\_br\_par           | False      | False          | ()            | False        |
|  228 | \_br\_flw\_imp\_r\_par           | False      | False          | ()            | False        |
|  229 | \_br\_flw\_imp\_br\_par          | False      | False          | ()            | False        |
|  230 | \_r\_sgl\_flw\_imp\_par          | False      | False          | ()            | False        |
|  231 | \_r\_flw\_jsl\_ann\_par          | False      | False          | ()            | False        |
|  232 | \_br\_flw\_jsl\_ann\_par         | False      | False          | ()            | False        |
|  233 | \_r\_sgl\_flw\_jsl\_ann\_par     | False      | False          | ()            | False        |
|  234 | \_r\_flw\_njl\_ann\_par          | False      | False          | ()            | False        |
|  235 | \_br\_flw\_njl\_ann\_par         | False      | False          | ()            | False        |
|  236 | \_r\_sgl\_flw\_njl\_ann\_par     | False      | False          | ()            | False        |
|  237 | \_flw\_ann\_par\_tal             | False      | False          | ()            | False        |
|  238 | \_sgl\_flw\_ann\_par\_tal        | False      | False          | ()            | False        |
|  239 | flow\_node                       | True       | True           | ()            | True         |
|  240 | flow\_node                       | True       | True           | ()            | True         |
|  241 | flow\_node                       | True       | True           | ()            | True         |
|  242 | flow\_node                       | True       | True           | ()            | True         |
|  243 | flow\_node                       | True       | True           | ()            | True         |
|  244 | double\_quote\_scalar            | True       | True           | ()            | True         |
|  245 | double\_quote\_scalar            | True       | True           | ()            | True         |
|  246 | double\_quote\_scalar            | True       | True           | ()            | True         |
|  247 | double\_quote\_scalar            | True       | True           | ()            | True         |
|  248 | double\_quote\_scalar            | True       | True           | ()            | True         |
|  249 | \_r\_sgl\_dqt\_ctn               | False      | False          | ()            | False        |
|  250 | \_br\_mtl\_dqt\_ctn              | False      | False          | ()            | False        |
|  251 | flow\_node                       | True       | True           | ()            | True         |
|  252 | flow\_node                       | True       | True           | ()            | True         |
|  253 | flow\_node                       | True       | True           | ()            | True         |
|  254 | flow\_node                       | True       | True           | ()            | True         |
|  255 | flow\_node                       | True       | True           | ()            | True         |
|  256 | single\_quote\_scalar            | True       | True           | ()            | True         |
|  257 | single\_quote\_scalar            | True       | True           | ()            | True         |
|  258 | single\_quote\_scalar            | True       | True           | ()            | True         |
|  259 | single\_quote\_scalar            | True       | True           | ()            | True         |
|  260 | single\_quote\_scalar            | True       | True           | ()            | True         |
|  261 | \_r\_sgl\_sqt\_ctn               | False      | False          | ()            | False        |
|  262 | \_br\_mtl\_sqt\_ctn              | False      | False          | ()            | False        |
|  263 | flow\_node                       | True       | True           | ()            | True         |
|  264 | flow\_node                       | True       | True           | ()            | True         |
|  265 | flow\_node                       | True       | True           | ()            | True         |
|  266 | flow\_node                       | True       | True           | ()            | True         |
|  267 | flow\_node                       | True       | True           | ()            | True         |
|  268 | flow\_node                       | True       | True           | ()            | True         |
|  269 | flow\_node                       | True       | True           | ()            | True         |
|  270 | flow\_node                       | True       | True           | ()            | True         |
|  271 | plain\_scalar                    | True       | True           | ()            | True         |
|  272 | plain\_scalar                    | True       | True           | ()            | True         |
|  273 | plain\_scalar                    | True       | True           | ()            | True         |
|  274 | plain\_scalar                    | True       | True           | ()            | True         |
|  275 | plain\_scalar                    | True       | True           | ()            | True         |
|  276 | plain\_scalar                    | True       | True           | ()            | True         |
|  277 | plain\_scalar                    | True       | True           | ()            | True         |
|  278 | plain\_scalar                    | True       | True           | ()            | True         |
|  279 | plain\_scalar                    | True       | True           | ()            | True         |
|  280 | flow\_node                       | True       | True           | ()            | True         |
|  281 | flow\_node                       | True       | True           | ()            | True         |
|  282 | flow\_node                       | True       | True           | ()            | True         |
|  283 | alias                            | True       | True           | ()            | True         |
|  284 | alias                            | True       | True           | ()            | True         |
|  285 | alias                            | True       | True           | ()            | True         |
|  286 | anchor                           | True       | True           | ()            | True         |
|  287 | anchor                           | True       | True           | ()            | True         |
|  288 | anchor                           | True       | True           | ()            | True         |
|  289 | \_drs\_doc\_repeat1              | False      | False          | ()            | False        |
|  290 | \_s\_dir\_rsv\_repeat1           | False      | False          | ()            | False        |
|  291 | \_r\_blk\_seq\_repeat1           | False      | False          | ()            | False        |
|  292 | \_r\_blk\_map\_repeat1           | False      | False          | ()            | False        |
|  293 | \_r\_blk\_str\_repeat1           | False      | False          | ()            | False        |
|  294 | \_r\_flw\_seq\_dat\_repeat1      | False      | False          | ()            | False        |
|  295 | \_r\_flw\_map\_dat\_repeat1      | False      | False          | ()            | False        |
|  296 | \_r\_sgl\_flw\_col\_dat\_repeat1 | False      | False          | ()            | False        |
|  297 | \_r\_dqt\_str\_repeat1           | False      | False          | ()            | False        |
|  298 | \_br\_mtl\_dqt\_ctn\_repeat1     | False      | False          | ()            | False        |
|  299 | \_r\_sqt\_str\_repeat1           | False      | False          | ()            | False        |
|  300 | \_br\_mtl\_sqt\_ctn\_repeat1     | False      | False          | ()            | False        |

## Fields

|   id | name   |
|------|--------|
|    0 | `None` |
|    1 | key    |
