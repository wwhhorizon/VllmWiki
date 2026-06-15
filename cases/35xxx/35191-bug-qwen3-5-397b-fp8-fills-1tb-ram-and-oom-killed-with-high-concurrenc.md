# vllm-project/vllm#35191: [Bug]: Qwen3.5 397B FP8 fills 1TB RAM and OOM killed with high-concurrency multimodal requests

| 字段 | 值 |
| --- | --- |
| Issue | [#35191](https://github.com/vllm-project/vllm/issues/35191) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 38; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 397B FP8 fills 1TB RAM and OOM killed with high-concurrency multimodal requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My vLLM instance fills up RAM while under high concurrent multimodal inputs. After it filled 1TB it is OOM killed by SLURM. Request pattern: 1 image per input: ~900 token, structured output with ~90 tokens, 50 concurrent requests for hours, from time to time also requests from other users out of my control. Setup: 4x H200 ``` vllm serve /mnt/models/Qwen_Qwen3.5-397B-A17B-FP8 \ --served-model-name Qwen3.5-397B-A17B-FP8 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.95 \ --enable-prefix-caching \ --mm-processor-cache-gb 10 \ --mm-processor-cache-type shm \ --mm-encoder-tp-mode data \ --max-num-batched-tokens 16384 ``` Observation: My input prompt is highly repetitive. At the beginning I have high MM & Prefix cache hit rates, but after an hour it is down to both 0% hit rate (my input should still have high hit rate). And then RAM fills up linearly up to 1TB. Currently the memory resource is restricted by SLURM for the vLLM instance to 1TB. A few weeks ago I saw the same problem with these inputs with Qwen3 VL 235B Thinking FP8 - it fille...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5 397B FP8 fills 1TB RAM and OOM killed with high-concurrency multimodal requests bug ### Your current environment ### 🐛 Describe the bug My vLLM instance fills up RAM while under high concurrent multimodal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5 397B FP8 fills 1TB RAM and OOM killed with high-concurrency multimodal requests bug ### Your current environment ### 🐛 Describe the bug My vLLM instance fills up RAM while under high concurrent multimodal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 5 397B FP8 fills 1TB RAM and OOM killed with high-concurrency multimodal requests bug ### Your current environment ### 🐛 Describe the bug My vLLM instance fills up RAM while under high concurrent multimodal inputs. Afte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
