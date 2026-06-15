# vllm-project/vllm#30624: [Bug]: `masked_scatter_size_check` failed when running Qwen3VLMoE

| 字段 | 值 |
| --- | --- |
| Issue | [#30624](https://github.com/vllm-project/vllm/issues/30624) |
| 状态 | closed |
| 标签 | bug;qwen;nvidia |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `masked_scatter_size_check` failed when running Qwen3VLMoE

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi team! I was trying to run Qwen3-VL-235B-A22B-Instruct-NVFP4 on a single B200 but encountered this problem: The command to launch vllm server: ``` uv run vllm serve --port 53705 --model RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 --async-scheduling --max-model-len 32768 --max-num-seqs 1024 --gpu-memory-utilization 0.85 --cudagraph-capture-sizes 1 2 4 8 16 24 32 40 48 56 64 72 80 88 96 104 112 120 128 136 144 152 160 168 176 184 192 200 208 216 224 232 240 248 256 272 288 304 320 336 352 368 384 400 416 432 448 464 480 496 512 1024 2048 4096 8192 ``` The benchmark script: ``` uv run vllm bench serve --backend openai-chat --base-url http://0.0.0.0:53705/ --endpoint /v1/chat/completions --model RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 --dataset-name random-mm --random-input-len 300 --random-output-len 200 --random-mm-base-items-per-request 1 --random-mm-num-mm-items-range-ratio 0 --num-prompts 10000 --random-mm-limit-mm-per-prompt '{"image": 1}' --ignore-eos --random-mm-bucket-config '{(512,512,1):1.0}' ``` Error Message: ``` /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:402: masked_scatter_size_check: block: [0,0,0], thread:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `masked_scatter_size_check` failed when running Qwen3VLMoE bug;qwen;nvidia ### Your current environment ### 🐛 Describe the bug Hi team! I was trying to run Qwen3-VL-235B-A22B-Instruct-NVFP4 on a single B200 but e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: scribe the bug Hi team! I was trying to run Qwen3-VL-235B-A22B-Instruct-NVFP4 on a single B200 but encountered this problem: The command to launch vllm server: ``` uv run vllm serve --port 53705 --model RedHatAI/Qwen3-V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: team! I was trying to run Qwen3-VL-235B-A22B-Instruct-NVFP4 on a single B200 but encountered this problem: The command to launch vllm server: ``` uv run vllm serve --port 53705 --model RedHatAI/Qwen3-VL-235B-A22B-Instru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: aten/src/ATen/native/cuda/IndexKernel.cu:402: masked_scatter_size_check: block: [0,0,0], thread: [0,0,0] Assertion `totalElements <= srcSize` failed. Error: Failed to initialize the TMA descriptor due to device-side ass...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
