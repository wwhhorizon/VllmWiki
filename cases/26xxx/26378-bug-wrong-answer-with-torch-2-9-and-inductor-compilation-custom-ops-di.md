# vllm-project/vllm#26378: [Bug]: Wrong answer with torch==2.9 and Inductor compilation (custom ops disabled)

| 字段 | 值 |
| --- | --- |
| Issue | [#26378](https://github.com/vllm-project/vllm/issues/26378) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 31; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wrong answer with torch==2.9 and Inductor compilation (custom ops disabled)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following command runs with 2.8 and fails with 2.9 (otherwise same environment): ``` python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --max-model-len=1024 ``` Output for 2.8: ``` INFO 10-07 14:02:25 [llm.py:310] Supported_tasks: ['generate'] WARNING 10-07 14:02:26 [model.py:1426] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`. Adding requests: 100%|██████████████████████████████████████████████████| 4/4 [00:01<00:00, 3.64it/s] Processed prompts: 0%| | 0/4 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]INFO 10-07 14:03:22 [loggers.py:127] Engine 000: Avg prompt throughput: 0.5 tokens/s, Avg generation throughput: 0.2 tokens/s, Running: 4 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% Processed prompts: 100%|█| 4/4 [00:55<00:00, 13.95s/it, est. speed input: 0.47 toks/s, output: 1.15 to -------------------------------------------------- Prompt: 'Hello, my nam...

## 现有链接修复摘要

#43727 [MoE] Remove inplace fused experts mechanism

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: with torch==2.9 and Inductor compilation (custom ops disabled) bug;torch.compile ### Your current environment ### 🐛 Describe the bug The following command runs with 2.8 and fails with 2.9 (otherwise same environment): `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d, please relaunch vLLM instance with `--generation-config vllm`. Adding requests: 100%|██████████████████████████████████████████████████| 4/4 [00:01<00:00, 3.64it/s] Processed prompts: 0%| | 0/4 [00:00<?, ?it/s, est....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --max-model-len=1024 ``` Output for 2.8: ``` INFO 10-07 14:02:25 [llm.py:310] Supported_tasks: ['generate'] WARNING 10-07 14:02:26 [model.py:1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: re exiting. ``` I also tried with `VLLM_USE_STANDALONE_COMPILE=0/1` and CUDA versions 12.8 and 13.0, same result in all cases. I get a correct output with `-O.custom_ops+=all`. cc @huydhn @zou3519 @Lucaskabela @atalman...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment): ``` python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --max-model-len=1024 ``` Output for 2.8: ``` INFO 10-07 14:02:25 [llm.py:310] Supported_tasks: ['ge...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43727](https://github.com/vllm-project/vllm/pull/43727) | mentioned | 0.6 | [MoE] Remove inplace fused experts mechanism | sharp edge: it is exactly the construct that broke under Inductor in #26378, and similar regressions are easy to land while the op remains registered. This PR executes the existin… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
