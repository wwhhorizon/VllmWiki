# vllm-project/vllm#14186: [Bug]: vllm 多节点部署问题

| 字段 | 值 |
| --- | --- |
| Issue | [#14186](https://github.com/vllm-project/vllm/issues/14186) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 多节点部署问题

### Issue 正文摘录

### Your current environment 问题如下 1、尝试两台服务器，进行多节点多 GPU（张量并行加管道并行推理），每台服务器各一个RTX4060 在配置完docker拉取镜像，并安装nvidia-container-toolkit驱动后 分别运行run_cluster.sh脚本 bash run_cluster.sh \ vllm/vllm-openai \ 111.6.168.225 \ --head \ /home/funhpc/dir \ -e VLLM_HOST_IP=111.6.168.225 bash run_cluster.sh \ vllm/vllm-openai \ 111.6.168.225 \ --worker \ /home/funhpc/model/dir \ -e VLLM_HOST_IP=111.6.168.235 启动成功，进入容器后通过ray status查看，显示如下 再进行服务启动vllm serve /root/.cache/huggingface --tensor-parallel-size 2 张量并行、流水线并行均不可，设置成1也不可，仅可任何参数不带的运行 vllm serve /root/.cache/huggingface 若指定为2，这时候遇到如下问题 2025-03-03 22:56:06,173 INFO worker.py:1636 -- Connecting to existing Ray cluster at address: 172.16.1.2:6379... 2025-03-03 22:56:06,190 INFO worker.py:1821 -- Connected to Ray cluster. (autoscaler +13s) Tip: use `ray status` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0. (autoscaler +13s) Error: No available node types can fulfill resource request {'node:111.6.168.225': 0.001, 'GPU': 1.0}. Add suitable node types to this cluster to resolve this issue. INFO 03-03 22:56:16 ray_utils.py:221] Waiting for creating a placement group of specs for 10 seconds. specs=[{'node:111.6.168.22...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tus` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0. (autoscaler +13s) Error: No available node types can fulfill resource request {'node:111.6.168.225': 0.001, 'GPU': 1.0}. Add s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: environment 问题如下 1、尝试两台服务器，进行多节点多 GPU（张量并行加管道并行推理），每台服务器各一个RTX4060 在配置完docker拉取镜像，并安装nvidia-container-toolkit驱动后 分别运行run_cluster.sh脚本 bash run_cluster.sh \ vllm/vllm-openai \ 111.6.168.225 \ --head \ /home/funhpc/dir \
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: our current environment 问题如下 1、尝试两台服务器，进行多节点多 GPU（张量并行加管道并行推理），每台服务器各一个RTX4060 在配置完docker拉取镜像，并安装nvidia-container-toolkit驱动后 分别运行run_cluster.sh脚本 bash run_cluster.sh \ vllm/vllm-openai \ 111.6.168.225 \ --head \ /home/f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 111.6.168.225 \ --worker \ /home/funhpc/model/dir \ -e VLLM_HOST_IP=111.6.168.235 启动成功，进入容器后通过ray status查看，显示如下 再进行服务启动vllm serve /root/.cache/huggingface --tensor-parallel-size 2 张量并行、流水线并行均不可，设置成1也不可，仅可任何参数不带的运行 vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 03-03 22:56:06,190 INFO worker.py:1821 -- Connected to Ray cluster. (autoscaler +13s) Tip: use `ray status` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0. (autoscaler +13s) Error...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
