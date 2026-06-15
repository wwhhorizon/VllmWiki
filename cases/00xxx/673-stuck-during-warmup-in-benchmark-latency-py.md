# vllm-project/vllm#673: Stuck during warmup in benchmark_latency.py

| 字段 | 值 |
| --- | --- |
| Issue | [#673](https://github.com/vllm-project/vllm/issues/673) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Stuck during warmup in benchmark_latency.py

### Issue 正文摘录

I'm trying to run the latency benchmark and am getting stuck. Am I using it correctly? ``` $ python benchmark_latency.py --model=meta-llama/Llama-2-7b-hf --tokenizer=hf-intern al-testing/llama-tokenizer --n 100 Namespace(model='meta-llama/Llama-2-7b-hf', tokenizer='hf-internal-testing/llama-tokenizer', tensor_parallel_size=1, input_ len=32, output_len=128, batch_size=8, n=100, use_beam_search=False, num_iters=3, trust_remote_code=False) INFO 08-03 21:56:59 llm_engine.py:70] Initializing an LLM engine with config: model='meta-llama/Llama-2-7b-hf', tokenizer=' hf-internal-testing/llama-tokenizer', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights= False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-03 21:56:59 tokenizer.py:29] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. /mnt/ml/vllm/vllm/worker/worker.py:231: UserWarning: The torch.cuda.*DtypeTensor constructors are no longer recommended. It 's best to use methods such as torch.tensor(data, dtype=*, d...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing stuck. Am I using it correctly? ``` $ python benchmark_latency.py --model=meta-llama/Llama-2-7b-hf --tokenizer=hf-intern al-testing/llama-tokenizer --n 100 Namespace(model='meta-llama/Llama-2-7b-hf',
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Stuck during warmup in benchmark_latency.py I'm trying to run the latency benchmark and am getting stuck. Am I using it correctly? ``` $ python benchmark_latency.py --model=meta-llama/Llama-2-7b-hf --tokenizer=hf-intern...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 1, input_ len=32, output_len=128, batch_size=8, n=100, use_beam_search=False, num_iters=3, trust_remote_code=False) INFO 08-03 21:56:59 llm_engine.py:70] Initializing an LLM engine with config: model='meta-llama/Llama-2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -testing/llama-tokenizer', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights= False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-03 21:56:59 tokeni...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l_size=1, input_ len=32, output_len=128, batch_size=8, n=100, use_beam_search=False, num_iters=3, trust_remote_code=False) INFO 08-03 21:56:59 llm_engine.py:70] Initializing an LLM engine with config: model='meta-llama/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
