# vllm-project/vllm#3390: (core dumped) when running `vllm` with `AWQ` on `MIG` partition of a H100 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#3390](https://github.com/vllm-project/vllm/issues/3390) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> (core dumped) when running `vllm` with `AWQ` on `MIG` partition of a H100 GPU

### Issue 正文摘录

This scripts [which work when MIG is disabled, crashes when MIG is enabled ](https://www.scaleway.com/en/docs/compute/gpu/how-to/use-nvidia-mig-technology/) Also reducing the number of prompts crashes too. It will always crash at the last prompt. When running another model like `llm = LLM(model="facebook/opt-125m", kv_cache_dtype="fp8_e5m2", max_model_len=2048)` this does not happen. # Reproduction On a H100 with MIG available ```bash # setup MIG sudo nvidia-smi -i 0 -mig 1 nvidia-smi mig -cgi 19,19,19,19,19,19,19 -C # install vllm pip install vllm # run the script below python reproduction.py ``` ```python # filename: reproduction.py from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", "Write a story about dinosors", "What is 291 - 1500?", ] prompt_template=''' [INST] {prompt} [/INST] ''' prompts = [prompt_template.format(prompt=prompt) for prompt in prompts] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=2496) llm = LLM(model="TheBloke/Mistral-7B-Instruct-v0.2-AWQ", quantization="awq", dtype="auto", max_model_len=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: way.com/en/docs/compute/gpu/how-to/use-nvidia-mig-technology/) Also reducing the number of prompts crashes too. It will always crash at the last prompt. When running another model like `llm = LLM(model="facebook/opt-125...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ich work when MIG is disabled, crashes when MIG is enabled ](https://www.scaleway.com/en/docs/compute/gpu/how-to/use-nvidia-mig-technology/) Also reducing the number of prompts crashes too. It will always crash at the l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: (core dumped) when running `vllm` with `AWQ` on `MIG` partition of a H100 GPU stale This scripts [which work when MIG is disabled, crashes when MIG is enabled ](https://www.scaleway.com/en/docs/compute/gpu/how-to/use-nv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: shes too. It will always crash at the last prompt. When running another model like `llm = LLM(model="facebook/opt-125m", kv_cache_dtype="fp8_e5m2", max_model_len=2048)` this does not happen. # Reproduction On a H100 wit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2496, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantiza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
