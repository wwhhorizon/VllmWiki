# vllm-project/vllm#7678: [Feature]: Please Support FATRelu

| 字段 | 值 |
| --- | --- |
| Issue | [#7678](https://github.com/vllm-project/vllm/issues/7678) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Please Support FATRelu

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #### When I tried to deploy `openbmb/ProSparse-MiniCPM-1B-sft`, it raised an error: ``` File "/home/xxxxxx/.conda/envs/vllm_env/lib/python3.10/site-packages/vllm/model_executor/models/minicpm.py", line 290, in __init__ self.mlp = MiniCPMMLP( File "/home/xxxxxx/.conda/envs/vllm_env/lib/python3.10/site-packages/vllm/model_executor/models/minicpm.py", line 166, in __init__ raise ValueError(f"Unsupported activation: {hidden_act}. " ValueError: Unsupported activation: fatrelu. Only silu is supported for now. ``` #### Here is the scripts: ``` #!/bin/bash set -e source ~/.bashrc conda activate vllm_env port=${1:-"8010"} devices=${2:-"6,7"} model_name=${3:-"LOCAL_PATH/ProSparse-MiniCPM-1B-sft"} export CUDA_VISIBLE_DEVICES="$devices" vllm serve ${model_name} --port $port --trust-remote-code ``` #### Packages: -torch2.4.0 -vllm0.5.4 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: {2:-"6,7"} model_name=${3:-"LOCAL_PATH/ProSparse-MiniCPM-1B-sft"} export CUDA_VISIBLE_DEVICES="$devices" vllm serve ${model_name} --port $port --trust-remote-code ``` #### Packages: -torch2.4.0 -vllm0.5.4 ### Alternativ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ile "/home/xxxxxx/.conda/envs/vllm_env/lib/python3.10/site-packages/vllm/model_executor/models/minicpm.py", line 290, in __init__ self.mlp = MiniCPMMLP( File "/home/xxxxxx/.conda/envs/vllm_env/lib/python3.10/site-packag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Please Support FATRelu feature request ### 🚀 The feature, motivation and pitch #### When I tried to deploy `openbmb/ProSparse-MiniCPM-1B-sft`, it raised an error: ``` File "/home/xxxxxx/.conda/envs/vllm_env/l...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
