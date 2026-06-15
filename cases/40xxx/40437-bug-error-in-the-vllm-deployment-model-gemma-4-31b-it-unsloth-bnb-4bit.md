# vllm-project/vllm#40437: [Bug]: error in the vllm deployment model gemma-4-31B-it-unsloth-bnb-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#40437](https://github.com/vllm-project/vllm/issues/40437) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: error in the vllm deployment model gemma-4-31B-it-unsloth-bnb-4bit

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I tried to deploy the gemma-4-31B-it-unsloth-bnb-4bit model through vllm, an error occurred during the deployment process。 My deployment command is as follows: ```text LD_LIBRARY_PATH=/data/miniforge3/envs/gemma4/lib:$LD_LIBRARY_PATH CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --model gemma-4-31B-it-unsloth-bnb-4bit/ --gpu-memory-utilization 0.6 --max-model-len 16392 --port 18003 --max-num-seqs 1 --enforce-eager --quantization bitsandbytes ``` The error message is as follows: ```text (EngineCore pid=49951) INFO 04-21 13:58:31 [gpu_model_runner.py:4820] Model loading took 19.61 GiB memory and 7.125814 seconds (EngineCore pid=49951) INFO 04-21 13:58:32 [gpu_model_runner.py:5753] Encoder cache will be initialized with a budget of 8192 tokens, and profiled with 3 video items of the maximum feature size. (EngineCore pid=49951) ERROR 04-21 13:58:46 [core.py:1108] EngineCore failed to start. (EngineCore pid=49951) ERROR 04-21 13:58:46 [core.py:1108] Traceback (most recent call last): (EngineCore pid=49951) ERROR 04-21 13:58:46 [core.py:1108] File "/data/miniforge3/envs/gemma4_unsloth/lib/python3.12/site-pack...

## 现有链接修复摘要

#40606 [Bugfix] Gemma-4: Add bnb QuantState alias hook on k_eq_v to load Gemma-4 BNB 4-bit weights

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: data/miniforge3/envs/gemma4_unsloth/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=49951) ERROR 04-21 13:58:46 [core.py:1108] return func(*args, **kwargs) (EngineCore pid=4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``text LD_LIBRARY_PATH=/data/miniforge3/envs/gemma4/lib:$LD_LIBRARY_PATH CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --model gemma-4-31B-it-unsloth-bnb-4bit/ --gpu-memory-utilization 0.6 --max-mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: error in the vllm deployment model gemma-4-31B-it-unsloth-bnb-4bit bug ### Your current environment ### 🐛 Describe the bug When I tried to deploy the gemma-4-31B-it-unsloth-bnb-4bit model through vllm, an error o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: .6 --max-model-len 16392 --port 18003 --max-num-seqs 1 --enforce-eager --quantization bitsandbytes ``` The error message is as follows: ```text (EngineCore pid=49951) INFO 04-21 13:58:31 [gpu_model_runner.py:4820] Model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: error in the vllm deployment model gemma-4-31B-it-unsloth-bnb-4bit bug ### Your current environment ### 🐛 Describe the bug When I tried to deploy the gemma-4-31B-it-unsloth-bnb-4bit model through vllm, an error o...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40606](https://github.com/vllm-project/vllm/pull/40606) | closes_keyword | 0.95 | [Bugfix] Gemma-4: Add bnb QuantState alias hook on k_eq_v to load Gemma-4 BNB 4-bit weights | Closes vllm-project/vllm#40437. When we load a Gemma 4 checkpoint that uses `--quantization bitsandbytes` and `attention_k_eq_v=true`, like `unsloth/gemma-4-31B-it-unsloth-bnb- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
