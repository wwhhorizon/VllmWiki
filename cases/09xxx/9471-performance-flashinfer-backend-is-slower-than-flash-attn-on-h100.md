# vllm-project/vllm#9471: [Performance]: FLASHINFER backend is slower than FLASH_ATTN on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#9471](https://github.com/vllm-project/vllm/issues/9471) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: FLASHINFER backend is slower than FLASH_ATTN on H100

### Issue 正文摘录

### Misc discussion on performance TLDR: We are observing that FP8 throughput is significantly lower when using `FLASHINFER` backend vs. using the default backend (`FLASH_ATTN`) for `llama3.1-8b` on a single H100 using `v0.6.4.dev22+g5b8a1fde`. Here is a simple repo script: ```python import vllm import transformers import time import numpy as np model = "neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8" input_size = 1024 output_size = 1024 batch_size = 64 llm = vllm.LLM( model=model, max_model_len=input_size+output_size, use_v2_block_manager=True, num_scheduler_steps=8, ) # create random batch np.random.seed(42) tokenizer = transformers.AutoTokenizer.from_pretrained(model) tokens = [ [] for _ in range(batch_size) ] for b in range(batch_size): for i in range(input_size): tokens[b].append(np.random.randint(tokenizer.vocab_size)) sampling_params = vllm.SamplingParams( max_tokens=output_size, ignore_eos=True, ) t0 = time.time() llm.generate( prompt_token_ids=tokens, sampling_params=sampling_params, use_tqdm=False ) t_elap = time.time()-t0 tput = batch_size * output_size / t_elap print("t_elap: %.2f seconds" % (t_elap)) print("throughput: %.2f tokens/second" % (tput)) ``` Running using `FLAS...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: sing `v0.6.4.dev22+g5b8a1fde`. Here is a simple repo script: ```python import vllm import transformers import time import numpy as np model = "neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8" input_size = 1024 output_size =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: FLASHINFER backend is slower than FLASH_ATTN on H100 performance ### Misc discussion on performance TLDR: We are observing that FP8 throughput is significantly lower when using `FLASHINFER` backend vs. us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g `FLASHINFER` backend vs. using the default backend (`FLASH_ATTN`) for `llama3.1-8b` on a single H100 using `v0.6.4.dev22+g5b8a1fde`. Here is a simple repo script: ```python import vllm import transformers import time...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: formance ### Misc discussion on performance TLDR: We are observing that FP8 throughput is significantly lower when using `FLASHINFER` backend vs. using the default backend (`FLASH_ATTN`) for `llama3.1-8b` on a single H1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Performance]: FLASHINFER backend is slower than FLASH_ATTN on H100 performance ### Misc discussion on performance TLDR: We are observing that FP8 throughput is significantly lower when using `FLASHINFER` backend vs. us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
