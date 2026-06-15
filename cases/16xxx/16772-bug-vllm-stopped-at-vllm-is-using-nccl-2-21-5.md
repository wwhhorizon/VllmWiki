# vllm-project/vllm#16772: [Bug]: vllm stopped at vLLM is using nccl==2.21.5

| 字段 | 值 |
| --- | --- |
| Issue | [#16772](https://github.com/vllm-project/vllm/issues/16772) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm stopped at vLLM is using nccl==2.21.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use two gpu to load the model, the vllm always stopped. But vllm works for one gpu inference. WARNING 04-17 17:24:41 [utils.py:2304] We must use the `spawn` multiprocessing start method. Overriding VLLM_WORKER_MULTIPROC_METHOD to 'spawn'. See https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#python-multiprocessing for more information. Reason: CUDA is initialized [2025-04-17 17:24:44,984] [INFO] [real_accelerator.py:239:get_accelerator] Setting ds_accelerator to cuda (auto detect) INFO 04-17 17:24:45 [__init__.py:239] Automatically detected platform cuda. INFO 04-17 17:24:47 [core.py:61] Initializing a V1 LLM engine (v0.8.4) with config: model='/home/users/tim.zhu/alphadrive/Qwen2.5-VL-7b', speculative_config=None, tokenizer='/home/users/tim.zhu/alphadrive/Qwen2.5-VL-7b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=3072, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=3072, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t environment ### 🐛 Describe the bug When I use two gpu to load the model, the vllm always stopped. But vllm works for one gpu inference. WARNING 04-17 17:24:41 [utils.py:2304] We must use the `spawn` multiprocessing st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: .8.4) with config: model='/home/users/tim.zhu/alphadrive/Qwen2.5-VL-7b', speculative_config=None, tokenizer='/home/users/tim.zhu/alphadrive/Qwen2.5-VL-7b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: roubleshooting.html#python-multiprocessing for more information. Reason: CUDA is initialized [2025-04-17 17:24:44,984] [INFO] [real_accelerator.py:239:get_accelerator] Setting ds_accelerator to cuda (auto detect) INFO 0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
