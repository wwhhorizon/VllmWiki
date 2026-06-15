# vllm-project/vllm#12872: [Bug]: Qwen2.5-VL-7B Instruct Lora model load failed

| 字段 | 值 |
| --- | --- |
| Issue | [#12872](https://github.com/vllm-project/vllm/issues/12872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-7B Instruct Lora model load failed

### Issue 正文摘录

### Your current environment vllm==0.7.2 transformers==4.49.0.dev0 ### 🐛 Describe the bug env CUDA_VISIBLE_DEVICES=0 vllm serve /data/Qwen/Qwen2.5-VL-7B-Instruct \ --served-model-name Qwen2___5-VL-7B-Instruct --limit-mm-per-prompt image=1 \ --max-model-len 16384 --dtype bfloat16 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8001 \ --trust-remote-code --max-num-batched-tokens 16384 --max-num-seqs 1 \ --enable-lora --max-loras 5 --lora-modules vl_lora=/home/sht/LLaMA-Factory-new-20250205/LLaMA-Factory-main/saves/Qwen2.5-VL-7B-Instruct/lora/vl_images_tags_v1_train_2025-02-05-14-28-34 Loading the Lora model reported the following error： [rank0]:[W207 15:18:18.529757338 ProcessGroupNCCL.cpp:1250] Warning: WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL. On normal program exit, the application should call destroy_process_group to ensure that any pending NCCL operations have finished in this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTorch 2.4 (function operator()) Traceback (most r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2.5-VL-7B Instruct Lora model load failed bug;stale ### Your current environment vllm==0.7.2 transformers==4.49.0.dev0 ### 🐛 Describe the bug env CUDA_VISIBLE_DEVICES=0 vllm serve /data/Qwen/Qwen2.5-VL-7B-Ins...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: VL-7B-Instruct --limit-mm-per-prompt image=1 \ --max-model-len 16384 --dtype bfloat16 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8001 \ --trust-remote-code --max-num-batched-tokens 16384 --max-num-seqs 1 \ --en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent vllm==0.7.2 transformers==4.49.0.dev0 ### 🐛 Describe the bug env CUDA_VISIBLE_DEVICES=0 vllm serve /data/Qwen/Qwen2.5-VL-7B-Instruct \ --served-model-name Qwen2___5-VL-7B-Instruct --limit-mm-per-prompt image=1 \ --m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rom_pretrained(model, model_id=LORA_PATH,adapter_name='vl_lora') model.eval() ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom rig...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.10/site-packages/vllm/scripts.py", line 204, in main args.dispatch_function(args) File "/home/sht/.conda/envs/glm4/lib/python3.10/site-packages/vllm/scripts.py", line 44, in serve uvloop.run(run_server(args))...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
