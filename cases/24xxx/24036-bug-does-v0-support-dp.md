# vllm-project/vllm#24036: [Bug]: Does V0 support DP?

| 字段 | 值 |
| --- | --- |
| Issue | [#24036](https://github.com/vllm-project/vllm/issues/24036) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Does V0 support DP?

### Issue 正文摘录

### Your current environment hardware: H20 image: v0.9.2 (https://hub.docker.com/layers/vllm/vllm-openai/v0.9.2/images/sha256-37cd5bd18d220a0f4c70401ce1d4a0cc588fbfe03cc210579428f2c47e6eac33) ### 🐛 Describe the bug I run Qwen3-30B-A3B with the following command(in docker container with this [image](https://hub.docker.com/layers/vllm/vllm-openai/v0.9.2/images/sha256-37cd5bd18d220a0f4c70401ce1d4a0cc588fbfe03cc210579428f2c47e6eac33) ) ```code VLLM_HOST_IP=$(hostname -I | awk '{print $1}') VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m vllm.entrypoints.openai.api_server --model /mnt/Qwen3-30B-A3B --port 8000 --max-model-len 10000 --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --data-parallel-size 8 ``` But I got the error ```text ERROR 09-01 02:20:44 [engine.py:458] Timed out after 601 seconds waiting for clients. 1/8 clients joined. ERROR 09-01 02:20:44 [engine.py:458] Traceback (most recent call last): ERROR 09-01 02:20:44 [engine.py:458] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine ERROR 09-01 02:20:44 [engine.py:458] engine = MQLLMEngine.from_vllm_config( ERROR 09-01 02:20:44 [engine.py:458]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e1d4a0cc588fbfe03cc210579428f2c47e6eac33) ### 🐛 Describe the bug I run Qwen3-30B-A3B with the following command(in docker container with this [image](https://hub.docker.com/layers/vllm/vllm-openai/v0.9.2/images/sha256-3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ) ```code VLLM_HOST_IP=$(hostname -I | awk '{print $1}') VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m vllm.entrypoints.openai.api_server --model /mnt/Qwen3-30B-A3B --port 8000 --max-model-len 10000 --gp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g ### Your current environment hardware: H20 image: v0.9.2 (https://hub.docker.com/layers/vllm/vllm-openai/v0.9.2/images/sha256-37cd5bd18d220a0f4c70401ce1d4a0cc588fbfe03cc210579428f2c47e6eac33) ### 🐛 Describe the bug I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ```text ERROR 09-01 02:20:44 [engine.py:458] Timed out after 601 seconds waiting for clients. 1/8 clients joined. ERROR 09-01 02:20:44 [engine.py:458] Traceback (most recent call last): ERROR 09-01 02:20:44 [engine.py:4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
