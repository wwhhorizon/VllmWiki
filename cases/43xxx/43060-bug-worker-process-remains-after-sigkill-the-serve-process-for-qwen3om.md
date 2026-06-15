# vllm-project/vllm#43060: [Bug]: worker process remains after SIGKILL the serve process for Qwen3omni model

| 字段 | 值 |
| --- | --- |
| Issue | [#43060](https://github.com/vllm-project/vllm/issues/43060) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: worker process remains after SIGKILL the serve process for Qwen3omni model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug /workspace/.venv/bin/python3 -m vllm_omni.entrypoints.cli.main serve /nvme1n1p1/models/Qwen/Qwen3-Omni-30B-A3B-Instruct --host 127.0.0.1 --port 53211 --omni --async-chunk --stage-init-timeout 600 --init-timeout 900 --log-stats --stage-configs-path /nvme1n1p1/xxx/vllm-omni-zmj-reli/vllm-omni/vllm_omni/deploy/qwen3_omni_moe.yaml ``` root 1 0 0 May12 pts/0 00:00:00 /bin/bash root 81 0 0 May12 pts/1 00:00:00 bash root 8060 0 0 May12 pts/2 00:00:00 bash root 530020 81 25 06:14 pts/1 00:02:01 /workspace/.venv/bin/python3 -m vllm_omni.entrypoints.cli.main serve /nvme1n1p1/models/Qwen/Qwen3-Omni-30B-A3B-Instruct --host 127. root 530283 530020 0 06:15 pts/1 00:00:00 /workspace/.venv/bin/python3 -c from multiprocessing.resource_tracker import main;main(57) root 530284 530020 23 06:15 pts/1 00:01:50 VLLM::StageEngineCoreProc_DP0 root 530287 530020 20 06:15 pts/1 00:01:33 VLLM::StageEngineCoreProc_DP0 root 531366 530020 19 06:16 pts/1 00:01:10 VLLM::StageEngineCoreProc_DP0 root 532096 8060 0 06:22 pts/2 00:00:00 ps -ef ``` kill -9 530020 ``` root 1 0 0 May12 pts/0 00:00:00 /bin/bash root 81 0 0 May12 pts/1 00:00:00 bash root 8060 0 0 May12 p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: worker process remains after SIGKILL the serve process for Qwen3omni model bug ### Your current environment ### 🐛 Describe the bug /workspace/.venv/bin/python3 -m vllm_omni.entrypoints.cli.main serve /nvme1n1p1/m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 00 /workspace/.venv/bin/python3 -c from multiprocessing.resource_tracker import main;main(57) root 530284 530020 23 06:15 pts/1 00:01:50 VLLM::StageEngineCoreProc_DP0 root 530287 530020 20 06:15 pts/1 00:01:33 VLLM::Sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: /nvme1n1p1/xxx/vllm-omni-zmj-reli/vllm-omni/vllm_omni/deploy/qwen3_omni_moe.yaml ``` root 1 0 0 May12 pts/0 00:00:00 /bin/bash root 81 0 0 May12 pts/1 00:00:00 bash root 8060 0 0 May12 pts/2 00:00:00 bash root 530020 81...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: FO: Started server process [530020] (APIServer pid=530020) INFO: Waiting for application startup. (APIServer pid=530020) INFO: Application startup complete. Killed ``` ### Before submitting a new issue... - [x] Make sur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
