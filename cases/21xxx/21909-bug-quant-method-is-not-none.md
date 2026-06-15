# vllm-project/vllm#21909: [Bug]: quant_method is not None

| 字段 | 值 |
| --- | --- |
| Issue | [#21909](https://github.com/vllm-project/vllm/issues/21909) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;moe;operator;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: quant_method is not None

### Issue 正文摘录

### Your current environment 2080ti * 2 Driver Version: 560.35.05 CUDA Version: 12.6 Name: vllm Version: 0.10.0 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,2 python -m vllm.entrypoints.openai.api_server --model /home/ma/work/modelscope/Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 2234 --tensor-parallel-size 2 --max-model-len 4096 --served-model-name gpt --served-model-name Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 --swap-space 16 --max-num-seqs 512 --trust-remote-code --disable-log-requests ## log info: Jul 30 06:54:50 ubuntu22lts bash[1239137]: INFO 07-30 06:54:50 [__init__.py:235] Automatically detected platform cuda. Jul 30 06:54:52 ubuntu22lts bash[1239137]: INFO 07-30 06:54:52 [api_server.py:1755] vLLM API server version 0.10.0 Jul 30 06:54:52 ubuntu22lts bash[1239137]: INFO 07-30 06:54:52 [cli_args.py:261] non-default args: {'host': '0.0.0.0', 'port': 2234, 'model': '/home/ma/work/modelscope/Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8', 'trust_remote_code': True, 'max_model_len': 8000, 'served_model_name': ['Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8'], 'tensor_parallel_size': 2, 'swap_space': 16.0, 'max_num_seqs': 512, 'disable_log_requests':...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: od is not None bug;stale ### Your current environment 2080ti * 2 Driver Version: 560.35.05 CUDA Version: 12.6 Name: vllm Version: 0.10.0 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,2 python -m vllm.entrypoints.openai....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Your current environment 2080ti * 2 Driver Version: 560.35.05 CUDA Version: 12.6 Name: vllm Version: 0.10.0 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,2 python -m vllm.entrypoints.openai.api_server --model /home/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: CUDA_VISIBLE_DEVICES=0,2 python -m vllm.entrypoints.openai.api_server --model /home/ma/work/modelscope/Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 2234 --tensor-parallel-size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: quant_method is not None bug;stale ### Your current environment 2080ti * 2 Driver Version: 560.35.05 CUDA Version: 12.6 Name: vllm Version: 0.10.0 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,2 python -m vllm.en...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: quant_method is not None bug;stale ### Your current environment 2080ti * 2 Driver Version: 560.35.05 CUDA Version: 12.6 Name: vllm Version: 0.10.0 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,2 python -m vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
