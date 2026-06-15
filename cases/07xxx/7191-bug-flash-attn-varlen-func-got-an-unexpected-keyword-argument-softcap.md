# vllm-project/vllm#7191: [Bug]: flash_attn_varlen_func() got an unexpected keyword argument 'softcap'

| 字段 | 值 |
| --- | --- |
| Issue | [#7191](https://github.com/vllm-project/vllm/issues/7191) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: flash_attn_varlen_func() got an unexpected keyword argument 'softcap'

### Issue 正文摘录

### Your current environment I built my flash-attn from the source. The version is 2.6.3 ### 🐛 Describe the bug When runing following code: ``` self.policy_model = LLM( model="OpenGVLab/InternVL2-8B", trust_remote_code=True, max_num_seqs=5, gpu_memory_utilization=0.40, ) ``` Raise the following error: [rank0]: TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'softcap'

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 6.3 ### 🐛 Describe the bug When runing following code: ``` self.policy_model = LLM( model="OpenGVLab/InternVL2-8B", trust_remote_code=True, max_num_seqs=5, gpu_memory_utilization=0.40, ) ``` Raise the following error: [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Your current environment I built my flash-attn from the source. The version is 2.6.3 ### 🐛 Describe the bug When runing following code: ``` self.policy_model = LLM( model="OpenGVLab/InternVL2-8B", trust_remote_code=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lash_attn_varlen_func() got an unexpected keyword argument 'softcap' bug;stale ### Your current environment I built my flash-attn from the source. The version is 2.6.3 ### 🐛 Describe the bug When runing following code:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
