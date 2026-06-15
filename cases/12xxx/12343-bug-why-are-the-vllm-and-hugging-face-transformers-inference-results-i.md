# vllm-project/vllm#12343: [Bug]: Why are the vLLM and Hugging Face Transformers inference results inconsistent?

| 字段 | 值 |
| --- | --- |
| Issue | [#12343](https://github.com/vllm-project/vllm/issues/12343) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Why are the vLLM and Hugging Face Transformers inference results inconsistent?

### Issue 正文摘录

### My current environment ### 🐛 Describe the bug Hello Team, I recently conducted inference using both vLLM and Hugging Face Transformers with the same model and input. However, I noticed that the output results were inconsistent between the two frameworks. Here are my questions regarding this issue: 1. What is the root cause of the inconsistency? 2. How can I align the inference results between the two frameworks to make them consistent? I look forward to your response. Thank you! Below are the experimental settings I have tried in an attempt to align the results, but the outputs are still inconsistent. I have also provided the code for reproduction. 1. Model: Phi3-mini-3.8B 2. Precision: BF16 3. Identical versions of PyTorch and FlashAttention2 4. No sampling strategy 5. Single GPU execution, no model parallelism 6. No batch (batch size = 1) 7. Inference is performed using the `generate` method from vLLM and Hugging Face on the same input question ```python import os from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM, AutoTokenizer os.environ["CUDA_VISIBLE_DEVICES"] = "0" model_path = 'microsoft/Phi-3-mini-4k-instruct' tokenizer = AutoTokenizer.f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: also provided the code for reproduction. 1. Model: Phi3-mini-3.8B 2. Precision: BF16 3. Identical versions of PyTorch and FlashAttention2 4. No sampling strategy 5. Single GPU execution, no model parallelism 6. No batch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: vided the code for reproduction. 1. Model: Phi3-mini-3.8B 2. Precision: BF16 3. Identical versions of PyTorch and FlashAttention2 4. No sampling strategy 5. Single GPU execution, no model parallelism 6. No batch (batch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: : Phi3-mini-3.8B 2. Precision: BF16 3. Identical versions of PyTorch and FlashAttention2 4. No sampling strategy 5. Single GPU execution, no model parallelism 6. No batch (batch size = 1) 7. Inference is performed using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion2 4. No sampling strategy 5. Single GPU execution, no model parallelism 6. No batch (batch size = 1) 7. Inference is performed using the `generate` method from vLLM and Hugging Face on the same input question ```pyt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed inference using both vLLM and Hugging Face Transformers with the same model and input. However, I noticed that the output results were inconsistent between the two frameworks. Here are my questions regarding this iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
