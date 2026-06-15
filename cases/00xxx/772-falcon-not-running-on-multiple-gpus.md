# vllm-project/vllm#772: Falcon not running on multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#772](https://github.com/vllm-project/vllm/issues/772) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Falcon not running on multiple GPUs

### Issue 正文摘录

Hi, I am trying to run Falcon on multiple GPUs. Below is the code for the same: `model_name = "tiiuae/falcon-7b-instruct" llm = LLM(model=model_name,trust_remote_code=True,dtype="float16",tensor_parallel_size=4) ` It's giving me the error: ` ValueError: Total number of attention heads (71) must be divisible by tensor parallel size (4). `Is there a way to resolve this issue ? It's working fine on A100 but I have four GPUs hence it is not working.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ae/falcon-7b-instruct" llm = LLM(model=model_name,trust_remote_code=True,dtype="float16",tensor_parallel_size=4) ` It's giving me the error: ` ValueError: Total number of attention heads (71) must be divisible by tensor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: size (4). `Is there a way to resolve this issue ? It's working fine on A100 but I have four GPUs hence it is not working. development attention_kv_cache;distributed_parallel;model_support attention dtype Hi, I am trying...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: trying to run Falcon on multiple GPUs. Below is the code for the same: `model_name = "tiiuae/falcon-7b-instruct" llm = LLM(model=model_name,trust_remote_code=True,dtype="float16",tensor_parallel_size=4) ` It's giving me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
