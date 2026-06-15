# vllm-project/vllm#3098: FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'  when trying prefix_pos parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#3098](https://github.com/vllm-project/vllm/issues/3098) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'  when trying prefix_pos parameter

### Issue 正文摘录

Run the codes ` outputs = llm.generate(prompts, sampling_params, prefix_pos=prefix_pos) ` to try the prefix cache. Got errors: ` FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig' ` I tried this within Vertex AI notebook, I confirmed that ldconfig was installed and executable. Any ideas?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ` I tried this within Vertex AI notebook, I confirmed that ldconfig was installed and executable. Any ideas?
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: m.generate(prompts, sampling_params, prefix_pos=prefix_pos) ` to try the prefix cache. Got errors: ` FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig' ` I tried this within Vertex AI notebook, I confirm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig' when trying prefix_pos parameter Run the codes ` outputs = llm.generate(prompts, sampling_params, prefix_pos=prefix_pos) ` to try the prefix cache. Got...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
