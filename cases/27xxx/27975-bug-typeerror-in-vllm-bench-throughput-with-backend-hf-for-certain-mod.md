# vllm-project/vllm#27975: [Bug]: TypeError in 'vllm bench throughput' with --backend hf for certain models (e.g., Qwen3)

| 字段 | 值 |
| --- | --- |
| Issue | [#27975](https://github.com/vllm-project/vllm/issues/27975) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError in 'vllm bench throughput' with --backend hf for certain models (e.g., Qwen3)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm bench throughput \ --model /nfs-vol/pvc-2c1664f0-8cf3-4774-bd6d-6029148f3779 \ --num-prompts 100 \ --input-len 128 \ --output-len 128 \ --seed 42 \ --max-model-len 512 \ --backend hf \ --hf-max-batch-size 8 When dataset path is not set, it will default to random dataset INFO 11-03 17:46:55 [datasets.py:614] Sampling input_len from [128, 128] and output_len from [128, 128] You have loaded an FP8 model on CPU and have a CUDA device available, make sure to set your model on a GPU device in order to run your model. To remove this warning, pass device_map = 'cuda'. Traceback (most recent call last): File "/root/trace-repo/vllm/.venv/bin/vllm", line 10, in sys.exit(main()) ^^^^^^ File "/root/trace-repo/vllm/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/root/trace-repo/vllm/vllm/entrypoints/cli/benchmark/throughput.py", line 21, in cmd main(args) File "/root/trace-repo/vllm/vllm/benchmarks/throughput.py", line 725, in main elapsed_time = run_hf( ^^^^^^^ File "/root/trace-repo/vllm/vllm/benchmarks/throughput.py", line 254, in run_hf llm = AutoModelForCausalLM.from_pretrained( ^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: TypeError in 'vllm bench throughput' with --backend hf for certain models (e.g., Qwen3) bug ### Your current environment ### 🐛 Describe the bug vllm bench throughput \ --model /nfs-vol/pvc-2c1664f0-8cf3-4774-bd6d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ut_len from [128, 128] and output_len from [128, 128] You have loaded an FP8 model on CPU and have a CUDA device available, make sure to set your model on a GPU device in order to run your model. To remove this warning,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: TypeError in 'vllm bench throughput' with --backend hf for certain models (e.g., Qwen3) bug ### Your current environment ### 🐛 Describe the bug vllm bench throughput \ --model /nfs-vol/pvc-2c1664f0-8cf3-4774-bd6d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: TypeError in 'vllm bench throughput' with --backend hf for certain models (e.g., Qwen3) bug ### Your current environment ### 🐛 Describe the bug vllm bench throughput \ --model /nfs-vol/pvc-2c1664f0-8cf3-4774-bd6d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: utput_len from [128, 128] You have loaded an FP8 model on CPU and have a CUDA device available, make sure to set your model on a GPU device in order to run your model. To remove this warning, pass device_map = 'cuda'. T...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
