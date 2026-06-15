# vllm-project/vllm#1062: GPU consumption

| 字段 | 值 |
| --- | --- |
| Issue | [#1062](https://github.com/vllm-project/vllm/issues/1062) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU consumption

### Issue 正文摘录

My environment involves creating a virtual machine (VM) on a Hyper Converge Infrastructure machine, and within the VM, setting up a Conda environment. And using an A100 80g GPU. Executing the following commands: python -m vllm.entrypoints.api_server --model 'LinkSoul/Chinese-Llama-2-7b' --swap-space 16 --disable-log-requests --host 172.22.119.190 --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 1 ![image](https://github.com/vllm-project/vllm/assets/39508634/de565359-80ec-4262-96fe-2a158cf1a865) GPU mem used 73GB! Can someone please tell me what cause it. Thanks

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ecuting the following commands: python -m vllm.entrypoints.api_server --model 'LinkSoul/Chinese-Llama-2-7b' --swap-space 16 --disable-log-requests --host 172.22.119.190 --port 10860 --max-num-seqs 256 --trust-remote-cod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the following commands: python -m vllm.entrypoints.api_server --model 'LinkSoul/Chinese-Llama-2-7b' --swap-space 16 --disable-log-requests --host 172.22.119.190 --port 10860 --max-num-seqs 256 --trust-remote-code --tens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: machine, and within the VM, setting up a Conda environment. And using an A100 80g GPU. Executing the following commands: python -m vllm.entrypoints.api_server --model 'LinkSoul/Chinese-Llama-2-7b' --swap-space 16 --disa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r --model 'LinkSoul/Chinese-Llama-2-7b' --swap-space 16 --disable-log-requests --host 172.22.119.190 --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 1 ![image](https://github.com/vllm-project/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
