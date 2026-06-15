# vllm-project/vllm#36489: [Bug]: vllm 0.17.0 部署 Qwen3.5 397b-fp8版本运行过程中异常崩溃(vllm 0.17.0 crashed unexpectedly during deployment of Qwen3.5 397b-fp8 version.)

| 字段 | 值 |
| --- | --- |
| Issue | [#36489](https://github.com/vllm-project/vllm/issues/36489) |
| 状态 | open |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.17.0 部署 Qwen3.5 397b-fp8版本运行过程中异常崩溃(vllm 0.17.0 crashed unexpectedly during deployment of Qwen3.5 397b-fp8 version.)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 运行一段时间后，出现下面日志后异常退出。运行设备A100，运行命令如下，vllm版本0.17.0版本。 After running for a period of time, the system crashed due to the following log entry. The command used was to run device A100, with vllm version 0.17.0. cmd： CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 nohup python3 -m vllm.entrypoints.openai.api_server --model "/models/Qwen3.5-397B-A17B-FP8" --served-model-name nuwa --port 60001 --enable-prefix-caching --tensor-parallel-size 8 --enable-auto-tool-choice --tool-call-parser qwen3_coder --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' --reasoning-parser qwen3 --gpu-memory-utilization 0.85 --language-model-only > vllmQwen35-397B.log 2>&1 & Below is the crash log: APIServer pid=2682023) INFO: 172.25.177.216:40184 - "GET /v1/models HTTP/1.1" 200 OK (EngineCore_DP0 pid=2682128) ERROR 03-09 19:11:40 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.17.0) with config: model='/models/Qwen3.5-397B-A17B-FP8', speculative_config=SpeculativeConfig(method='mtp', model='/models/Qwen3.5-397B-A17B-FP8', num_spec_tokens=2), tokenizer='/models/Qwen3.5-397B-A17B-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: rallel-size 8 --enable-auto-tool-choice --tool-call-parser qwen3_coder --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' --reasoning-parser qwen3 --gpu-memory-utilization 0.85 --language-mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: vllm 0.17.0 部署 Qwen3.5 397b-fp8版本运行过程中异常崩溃(vllm 0.17.0 crashed unexpectedly during deployment of Qwen3.5 397b-fp8 version.) bug ### Your current environment ### 🐛 Describe the bug 运行一段时间后，出现下面日志后异常退出。运行设备A100，运行命...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 溃(vllm 0.17.0 crashed unexpectedly during deployment of Qwen3.5 397b-fp8 version.) bug ### Your current environment ### 🐛 Describe the bug 运行一段时间后，出现下面日志后异常退出。运行设备A100，运行命令如下，vllm版本0.17.0版本。 After running for a period o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: current environment ### 🐛 Describe the bug 运行一段时间后，出现下面日志后异常退出。运行设备A100，运行命令如下，vllm版本0.17.0版本。 After running for a period of time, the system crashed due to the following log entry. The command used was to run device A1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm 0.17.0 部署 Qwen3.5 397b-fp8版本运行过程中异常崩溃(vllm 0.17.0 crashed unexpectedly during deployment of Qwen3.5 397b-fp8 version.) bug ### Your current environment ### 🐛 Describe the bug 运行一段时间后，出现下面日志后异常退出。运行设备A100，运行命...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
