# vllm-project/vllm#40802: [Feature]: Deepseek V4 cannot run ,Please support SM120 GPU,example rtx5090  rtxpro6000

| 字段 | 值 |
| --- | --- |
| Issue | [#40802](https://github.com/vllm-project/vllm/issues/40802) |
| 状态 | open |
| 标签 | feature request;DSv4 |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Deepseek V4 cannot run ,Please support SM120 GPU,example rtx5090  rtxpro6000

### Issue 正文摘录

### 🚀 The feature, motivation and pitch PS C:\Users\wuwen> docker run --gpus all --privileged --ipc=host -p 8005:8005 -e CUDA_DEVICE_ORDER=PCI_BUS_ID -e CUDA_VISIBLE_DEVICES=0,1 -e NCCL_CUMEM_ENABLE=0 -v I:\AI-Chat\models\Deepseek:/models vllm/vllm-openai:deepseekv4-cu130 /models/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --tensor-parallel-size 2 --attention_config.use_fp4_indexer_cache=True --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 --enable-auto-tool-choice --reasoning-parser deepseek_v4 --host 0.0.0.0 --served-model-name VLLM-MODEL --gpu-memory-utilization 0.95 --async-scheduling --enable-prefix-caching --max-num-seqs 2 (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:299] (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.1.dev15830+g8d599d76a (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:299] █▄█▀ █ █ █ █ model /models/DeepSeek-V4-Flash (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:299] (APIServer pid=1) INFO 04-24 10:27:00 [utils.py:233...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: eepseekv4-cu130 /models/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --tensor-parallel-size 2 --attention_config.use_fp4_indexer_cache=True --tokenizer-mode deepse...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: request;DSv4 ### 🚀 The feature, motivation and pitch PS C:\Users\wuwen> docker run --gpus all --privileged --ipc=host -p 8005:8005 -e CUDA_DEVICE_ORDER=PCI_BUS_ID -e CUDA_VISIBLE_DEVICES=0,1 -e NCCL_CUMEM_ENABLE=0 -v I:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cannot run ,Please support SM120 GPU,example rtx5090 rtxpro6000 feature request;DSv4 ### 🚀 The feature, motivation and pitch PS C:\Users\wuwen> docker run --gpus all --privileged --ipc=host -p 8005:8005 -e CUDA_DEVICE_O...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Feature]: Deepseek V4 cannot run ,Please support SM120 GPU,example rtx5090 rtxpro6000 feature request;DSv4 ### 🚀 The feature, motivation and pitch PS C:\Users\wuwen> docker run --gpus all --privileged --ipc=host -p 800...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor (APIServer pid=1) INFO 04-24 10:27:11 [scheduler.py:238] Chunked prefill is enabled with max_num_bat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
