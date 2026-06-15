# vllm-project/vllm#30142: [Bug]: `assert request.num_output_placeholders >= 0` can fail in async scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#30142](https://github.com/vllm-project/vllm/issues/30142) |
| 状态 | open |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `assert request.num_output_placeholders >= 0` can fail in async scheduling

### Issue 正文摘录

### Your current environment Currently using vLLM v0.12.0 (issue also seen on v0.11.2; not sure about older versions) with the official Docker image, on 8xH200 nodes. ### 🐛 Describe the bug Using the following command to launch vLLM: ```sh sudo docker run --gpus all --detach \ -e "VLLM_USE_DEEP_GEMM=1" \ -e "VLLM_MOE_USE_DEEP_GEMM=0" \ -e "CUDA_VISIBLE_DEVICES=4,5,6,7" \ -p 8235:8080 \ --ipc=host \ vllm/vllm-openai:v0.12.0 \ --host=0.0.0.0 \ --port=8080 \ --model=Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 \ --gpu-memory-utilization=0.95 \ --load-format=safetensors \ --max-num-seqs=64 \ --tensor-parallel-size 4 \ --seed=0 \ --served-model-name qwen3 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --async_scheduling ``` It happens that the following assertion fails (I assume only when async scheduling is enabled but I didn't try without; as the assertion can take a long time to fail). ``` (EngineCore_DP0 pid=396) ERROR 12-05 07:26:46 [core.py:845] EngineCore encountered a fatal error. (EngineCore_DP0 pid=396) ERROR 12-05 07:26:46 [core.py:845] Traceback (most recent call last): (EngineCore_DP0 pid=396) ERROR 12-05 07:26:46 [core.py:845] File "/usr/local/lib/python3.12/dist-pac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tly using vLLM v0.12.0 (issue also seen on v0.11.2; not sure about older versions) with the official Docker image, on 8xH200 nodes. ### 🐛 Describe the bug Using the following command to launch vLLM: ```sh sudo docker ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm/vllm-openai:v0.12.0 \ --host=0.0.0.0 \ --port=8080 \ --model=Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 \ --gpu-memory-utilization=0.95 \ --load-format=safetensors \ --max-num-seqs=64 \ --tensor-parallel-size 4 \ --see...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: `assert request.num_output_placeholders >= 0` can fail in async scheduling bug ### Your current environment Currently using vLLM v0.12.0 (issue also seen on v0.11.2; not sure about older versions) with the offici...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -e "VLLM_USE_DEEP_GEMM=1" \ -e "VLLM_MOE_USE_DEEP_GEMM=0" \ -e "CUDA_VISIBLE_DEVICES=4,5,6,7" \ -p 8235:8080 \ --ipc=host \ vllm/vllm-openai:v0.12.0 \ --host=0.0.0.0 \ --port=8080 \ --model=Qwen/Qwen3-235B-A22B-Instruct...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: vLLM: ```sh sudo docker run --gpus all --detach \ -e "VLLM_USE_DEEP_GEMM=1" \ -e "VLLM_MOE_USE_DEEP_GEMM=0" \ -e "CUDA_VISIBLE_DEVICES=4,5,6,7" \ -p 8235:8080 \ --ipc=host \ vllm/vllm-openai:v0.12.0 \ --host=0.0.0.0 \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
