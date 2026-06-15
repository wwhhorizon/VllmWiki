# vllm-project/vllm#10313: [Bug]: FusedMoE kernel performance depends on input prompt length while decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#10313](https://github.com/vllm-project/vllm/issues/10313) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;moe;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FusedMoE kernel performance depends on input prompt length while decoding

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Environment - H100 ### Description - FuseMoE kernel should not depend on the size of input prompts while decoding because there is no dependency with the input length, but output tokens/sec during decoding significantly changes in Mixtral model when we change input prompt length. It degrades around 50% when input length increases to x2. - To verify this, we just **commented out attention code** that has dependency with the lengths of input/output tokens in Mixtral model and confirmed that the results of Mixtral decoding speed degrade when the input prompt length increases even if the attention code was commented out. ### How to resolve - My guess was that there is some bug in the fused moe kernel, and took a look at the commit history of fused moe. There was a commit regarding improvement of fused moe performance (https://github.com/vllm-project/vllm/pull/9384), but I'm not sure this commit is the root cause of the bug. I just rolled back the version from latest to 0.6.3.post1 release. - In 0.6.3.post1 release version, the bug disappered. The decoding speed of Mixtral w/o attention does not...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t depend on the size of input prompts while decoding because there is no dependency with the input length, but output tokens/sec during decoding significantly changes in Mixtral model when we change input prompt length....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: el Input Dumps _No response_ ### 🐛 Describe the bug ### Environment - H100 ### Description - FuseMoE kernel should not depend on the size of input prompts while decoding because there is no dependency with the input len...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: MoE kernel performance depends on input prompt length while decoding bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Environment - H100 ### Description - FuseMoE ker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;moe;speculative_decoding attention;cuda;kernel;moe;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mpt length while decoding bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Environment - H100 ### Description - FuseMoE kernel should not depend on the size of input...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
