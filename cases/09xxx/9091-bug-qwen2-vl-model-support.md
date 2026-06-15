# vllm-project/vllm#9091: [Bug]: Qwen2-VL model support

| 字段 | 值 |
| --- | --- |
| Issue | [#9091](https://github.com/vllm-project/vllm/issues/9091) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2-VL model support

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I trying to start **Qwen/Qwen2-VL-72B-Instruct-AWQ** model with docker vllm. Server with 5 rtx 3090ti. Llama 70b and other models works fine. I have exception at downloading process. The same problem raises with **Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4** model. Vllm is latest v0.6.2. Strat in docker: `sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"device=1,2,3,4"' -p 9000:8000 --mount type=bind,source=/home/me/.cache,target=/root/.cache vllm/vllm-openai:v0.6.2 --model Qwen/Qwen2-VL-72B-Instruct-AWQ --tensor-parallel-size 4 --gpu-memory-utilization 0.92 --max-model-len 8000 --dtype half -q awq --disable-log-requests` Exception: ``` INFO 10-05 01:33:20 api_server.py:177] Started engine process with PID 77 config.json: 100%|██████████████████████████████████████████████████████████████████████████████| 1.39k/1.39k [00:00 ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 571, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the bug I trying to start **Qwen/Qwen2-VL-72B-Instruct-AWQ** model with docker vllm. Server with 5 rtx 3090ti. Llama 70b and other models works fine. I have exception at downloading process. The same problem raises with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2-VL model support bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I trying to start **Qwen/Qwen2-VL-72B-Instruct-AWQ** model with docker vllm. Server with 5 rtx 309
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: process. The same problem raises with **Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4** model. Vllm is latest v0.6.2. Strat in docker: `sudo docker run --ipc=host --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"dev...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: **Qwen/Qwen2-VL-72B-Instruct-AWQ** model with docker vllm. Server with 5 rtx 3090ti. Llama 70b and other models works fine. I have exception at downloading process. The same problem raises with **Qwen/Qwen2-VL-72B-Instr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -utilization 0.92 --max-model-len 8000 --dtype half -q awq --disable-log-requests` Exception: ``` INFO 10-05 01:33:20 api_server.py:177] Started engine process with PID 77 config.json: 100%|█████████████████████████████...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
