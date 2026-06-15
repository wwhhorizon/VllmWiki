# vllm-project/vllm#5240: [Bug]: Tokenizer setter of LLM without CachedTokenizer adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#5240](https://github.com/vllm-project/vllm/issues/5240) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tokenizer setter of LLM without CachedTokenizer adapter

### Issue 正文摘录

### Your current environment same to the issue [#5206](https://github.com/vllm-project/vllm/issues/5206) ### 🐛 Describe the bug As the basic reason of the issue reported by [#5206](https://github.com/vllm-project/vllm/issues/5206), the tokenizer setter of the LLM will override the cached tokenizer inited by llm_engine. ```python def set_tokenizer( self, tokenizer: Union[PreTrainedTokenizer, PreTrainedTokenizerFast], ) -> None: self.llm_engine.tokenizer.tokenizer = tokenizer ``` Thus, each time the ```len(tokenizer)``` is called, row ```__len__``` is called rather than the CachedTokenizer's. To fixed this problem of this issue, the ```get_cached_tokenizer``` adapter should be applied by the tokenizer setter of LLM.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
