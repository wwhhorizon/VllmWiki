# vllm-project/vllm#17954: [Bug]: prefix caching doesn't work on CPU vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#17954](https://github.com/vllm-project/vllm/issues/17954) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: prefix caching doesn't work on CPU vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I install CPU vLLM following this [guide](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html?device=x86#cpu) and run vllm serve with the `--enable-prefix-caching` parameter. ```bash vllm serve Qwen/Qwen2.5-1.5B-Instruct --enable-prefix-caching ``` Send inference requests like this: ```bash for i in {1..100}; do echo "Request: $i" curl -sS http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen2.5-1.5B-Instruct", "messages": [ {"role": "user", "content": "Tell me a joke"} ] }' echo "" done ``` According to the logs, it appears that the prefix caching does not work. `Prefix cache hit rate: GPU: 0.00%, CPU: 0.00%`. ```bash (vllm-cpu) root@demo:~/vllm_source# vllm serve Qwen/Qwen2.5-1.5B-Instruct --enable-prefix-caching [W511 12:03:43.958623328 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: CPU vLLM bug ### Your current environment ### 🐛 Describe the bug I install CPU vLLM following this [guide](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html?device=x86#cpu) and run vllm serve with the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: m serve with the `--enable-prefix-caching` parameter. ```bash vllm serve Qwen/Qwen2.5-1.5B-Instruct --enable-prefix-caching ``` Send inference requests like this: ```bash for i in {1..100}; do echo "Request: $i" curl -s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ve Qwen/Qwen2.5-1.5B-Instruct --enable-prefix-caching ``` Send inference requests like this: ```bash for i in {1..100}; do echo "Request: $i" curl -sS http://localhost:8000/v1/chat/completions \ -H "Content-Type: applic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
