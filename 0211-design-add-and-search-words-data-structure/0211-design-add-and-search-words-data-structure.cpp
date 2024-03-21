// #define _GLIBCXX_DEBUG 1
// #define _GLIBCXX_DEBUG_PEDANTIC 1  // use them if there is a bug you can not find
// #define _FORTIFY_SOURCE 2

#include <bits/stdc++.h>
// #pragma GCC optimize ("O3")// may make your code
// #pragma GCC target ("sse4")// faster, or might make it slower.
#include <math.h>

using namespace std;
typedef long long ll ;
typedef long double ld;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef pair<ld,ld> pd;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<ld> vd;
typedef vector<bool> vb;
typedef vector<char> vc;
typedef unordered_set<int> usi;
typedef unordered_set<ll> usl;
typedef unordered_map<int,int> umi;
typedef unordered_map<ll,ll> uml;
typedef set<int> si;
typedef set<ll> sl;
typedef map<int,int> mi;
typedef map<ll,ll> ml;
typedef tuple<int,int,int> tup;

// to use the function order_of_key() which returns the index of the key.
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp> 
typedef __gnu_pbds::tree<ll, __gnu_pbds::null_type, less<ll>, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update> ordered_set;

template<class T> using pq = priority_queue<T>;
template<class T> using pqs = priority_queue<T, vector<T>, greater<T>>;

template<class T> bool ckmin(T& a,T b) { return b < a ? a = b, 1 : 0; }
template<class T> bool ckmax(T& a,T b) { return a < b ? a = b, 1 : 0; }
template<class T,class V> bool in(V a,T x) { return find(x.begin(),x.end(),a)!=x.end();}
template<class T> string check(T a) { return a? "YES" : "NO"; }
template<class T> void append(T& a,T b) {a.insert(a.end(),b.begin(),b.end());}
template<class T,class V> bool add_overflow(T a,V b) {return (a>=0 && b>=0 || a<=0 && b<=0) && (abs(a)+abs(b))<abs(a)? 1:0;}
template<class T, class V> bool mul_overflow(T a,V b) {return b!=0 && (a*b)/b!=a? 1:0;}

#define all(x) x.begin(), x.end()
#define fori(i,start,end) for (int i=start; i<=end; i++)
#define ford(i,start,end) for (int i = start; i >= end; i--)
#define trav(a,x) for (auto& a : x)
 
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define sz(x) (int)(x).size()

const ll INF=LLONG_MAX;

// debuging tools
template <class T>
void print(T x){
    for (auto i:x) cout<<i<<" ";
    cout<<"\n";    
}
template <class T>
void print_map(T x){
    for (auto a:x)
    cout<<a.f<<" "<<a.s<<"\n";
}
// usefull functions
ll vec_to_bin(vb x){return accumulate(x.rbegin(), x.rend(), 0, [](int x, int y) { return (x << 1) + y; });}

template <class T> map<T,ll> count_occ(vector<T> x){
    map<T,ll> counter;
    for(auto a:x)counter[a]++;
    return counter;
}

vl get_prefix_sum(vl x){
    auto n=x.size();
    vl prefix_sum(n+1,0);
    for (int i=1;i<=n;i++)prefix_sum[i]=prefix_sum[i-1]+x[i-1];
    return prefix_sum;
}

vl get_prefix_xor(vl x){
    auto n=x.size();
    vl prefix_xor(n+1,0);
    for (int i=1;i<=n;i++)prefix_xor[i]=prefix_xor[i-1]^x[i-1];
    return prefix_xor;
}

vl get_suffix_sum(vl x){
    auto n=x.size();
    vl suffix_sum(n+1,0);
    for (int i=n-1;i>=0;i--)suffix_sum[i]=suffix_sum[i+1]+x[i];
    return suffix_sum;
}

ll square(ll x) {
    if (x>3037000499) return INF; // overflow.
    return x*x;
    }

ll custom_pow(ll x,ll n){
    if (n==0) return 1;
    if (n&1) {
        ll a=x,b=custom_pow(x,n-1);
        ll c=a*b;
        if (c/a!=b) return INF; // overflow
        return c;
    }
    return square(custom_pow(x,n/2));// This already handles overflow.
}

ll get_lower_bound_nth_root(ll x,ll n){
    ll low=0,high=x;
    while (low<=high)
    {
        ll mid=(low+high)>>1;
        if (custom_pow(mid,n)<x) low=mid+1;
        else high=mid-1;
    }
    return low;
}

ll get_upper_bound_nth_root(ll x,ll n){
    ll low=0,high=x;
    while (low<=high)
    {
        ll mid=(low+high)>>1;
        if (custom_pow(mid,n)<=x) low=mid+1;
        else high=mid-1;
    }
    return low;
}

ll get_perfect_square(ll x){
    ll low=0,high=x;
    while (low<=high)
    {
        ll mid=(low+high)>>1;
        if (square(mid)<x) low=mid+1;
        else high=mid-1;
    }
    return (low*low==x? low:-1);
}

ll pow_mod(ll x,ll n,ll mod){
    if (n==0) return 1%mod;
    if (n&1) return ((x%mod)*pow_mod(x,n-1,mod))%mod;
    return square(pow_mod(x,n/2,mod))%mod;
}


ll lcm(ll x,ll y){
    return (x/__gcd(x,y))*y;
}

ll custom_mod(ll x,ll mod){
    if (x>=0) return x%mod;
    return (x-(((x/mod)-1)*mod))%mod;
}
template <class T>
T get_subarray(T& x,int start, int end)// start and end are inculded
{
    T ans(x.begin()+start,x.begin()+end+1);
    return ans;
}

ld log_base(ld x, ld base) {return log2(x)/log2(base);}
ll custom_max(ll a, ll b){return max(a,b);}
ll custom_min(ll a, ll b){return min(a,b);}
ll custom_sum(ll a, ll b){return a+b;}

// cout<<setprecision(x)<<number with x floating points.

const ll mod=998244353;
const char nl='\n';
const char sp=' ';
// my code

class Trie{// only for a-z strings
    public:
    vector<vl> tree;ll next_free_node=0; vl cnt_end;
    Trie(){
        tree.pb(vl(26,-1));
        cnt_end.pb(0);
        next_free_node++;
    }
    string add_string(string x){
        string longest_common_prefix;
        bool keep_adding=true;
        ll current_node=0;
        trav(c,x){
            if (tree[current_node][c-'a']==-1) {
                tree.pb(vl(26,-1));
                cnt_end.pb(0);
                tree[current_node][c-'a']=next_free_node++;
                keep_adding=false;
            }
            current_node=tree[current_node][c-'a'];
            if (keep_adding) longest_common_prefix.pb(c);
        }
        cnt_end[current_node]++;
        return longest_common_prefix;
    }

    bool dfs(ll node,ll index, string & x){
        if (index==sz(x)) return cnt_end[node]>0;
        if (x[index]!='.' && tree[node][x[index]-'a']==-1) return false;
        if (x[index]!='.' && tree[node][x[index]-'a']!=-1) return dfs(tree[node][x[index]-'a'],index+1,x);
        bool ans=false;
        fori(i,0,25) if (tree[node][i]!=-1) ans|=dfs(tree[node][i],index+1,x);
        return ans;
    }

    bool find_string(string x){
        return dfs(0,0,x);
    }
};

class WordDictionary {
public:
    Trie t;
    WordDictionary() {
    }
    
    void addWord(string word) {
        t.add_string(word);
    }
    
    bool search(string word) {
        return t.find_string(word);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */