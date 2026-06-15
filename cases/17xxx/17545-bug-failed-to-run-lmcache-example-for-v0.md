# vllm-project/vllm#17545: [Bug]: failed to run LMCache example for v0

| 字段 | 值 |
| --- | --- |
| Issue | [#17545](https://github.com/vllm-project/vllm/issues/17545) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to run LMCache example for v0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run this example code after build both vllm and LMCache code see below error ``` root@salab-hpedl380g11-02:/mnt/nvme2n1/wayne/lmvllm/vllm/examples/lmcache# python cpu_offload_lmcache.py -v v0 INFO 05-01 17:46:20 [__init__.py:239] Automatically detected platform cuda. INFO 05-01 17:46:29 [config.py:751] This model supports multiple tasks: {'score', 'classify', 'embed', 'generate', 'reward'}. Defaulting to 'generate'. INFO 05-01 17:46:29 [config.py:2040] Chunked prefill is enabled with max_num_batched_tokens=8192. /mnt/nvme2n1/wayne/lmvllm/vllm/vllm/transformers_utils/tokenizer_group.py:23: FutureWarning: It is strongly recommended to run mistral models with `--tokenizer-mode "mistral"` to ensure correct encoding and decoding. self.tokenizer = get_tokenizer(self.tokenizer_id, **tokenizer_config) INFO 05-01 17:46:30 [core.py:59] Initializing a V1 LLM engine (v0.8.5.dev404+g98060b001) with config: model='mistralai/Mistral-7B-Instruct-v0.2', speculative_config=None, tokenizer='mistralai/Mistral-7B-Instruct-v0.2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rent environment ### 🐛 Describe the bug run this example code after build both vllm and LMCache code see below error ``` root@salab-hpedl380g11-02:/mnt/nvme2n1/wayne/lmvllm/vllm/examples/lmcache# python cpu_offload_lmca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: failed to run LMCache example for v0 bug;stale ### Your current environment ### 🐛 Describe the bug run this example code after build both vllm and LMCache code see below error ``` root@salab-hpedl380g11-02:/mnt/n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nit__.py:239] Automatically detected platform cuda. INFO 05-01 17:46:29 [config.py:751] This model supports multiple tasks: {'score', 'classify', 'embed', 'generate', 'reward'}. Defaulting to 'generate'. INFO 05-01 17:4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
