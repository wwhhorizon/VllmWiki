# vllm-project/vllm#16714: [Bug]: Can't set ray_workers_use_nsight for LLMengine

| 字段 | 值 |
| --- | --- |
| Issue | [#16714](https://github.com/vllm-project/vllm/issues/16714) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't set ray_workers_use_nsight for LLMengine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I can be sure that `ray_workers_use_nsight` worked for me at first. But after a certain time when I'm using nsys to profile a LLM process and it got stuck, I press ctrl-Z to stop it, but he no longer worked. Now if `ray_workers_use_nsight=False` it boots normally, but `ray_workers_use_nsight=True` causes it to stuch when initialize nccl environment and warn is generated as below: ada6000-02:165062:165062 [0] NCCL INFO Failed to open libibverbs.so[.1] ada6000-02:165062:165062 [0] NCCL INFO NET/Socket : Using [0]enp3s0f0:10.2.64.94 [1]usb0:169.254.3.1 [2]virbr0:192.168.122.1 [3]vethba72486:fe80::604b:61ff:fed0:3cd7%vethba72486 [4]veth7c73dea:fe80::3c9d:c3ff:fe9a:d1f8%veth7c73dea [5]vethdab3b18:fe80::6495:c4ff:fe68:3310%vethdab3b18 [6]veth0f7a669:fe80::185b:27ff:fee8:b05f%veth0f7a669 [7]vethea5e805:fe80::c893:20ff:feef:1810%vethea5e805 ada6000-02:165062:165062 [0] NCCL INFO Using non-device net plugin version 0 ada6000-02:165062:165062 [0] NCCL INFO Using network Socket ada6000-02:165062:166441 [0] bootstrap.cc:77 NCCL WARN Message truncated : received 172 bytes instead of 64 ada6000-02:165062:166441 [0] NCCL INFO bootstrap.cc:130 -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ada6000-02:165062:165062 [0] NCCL INFO Using non-device net plugin version 0 ada6000-02:165062:165062 [0] NCCL INFO Using network Socket ada6000-02:165062:166441 [0] bootstrap.cc:77 NCCL WARN Message truncated : receive...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: principles of Ray, and I'd like to ask if there is some kind of relationship between nsys, NCCL, and Ray that causes this change. Addendum: I'm currently using docker and I don't know if this information will help me wi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: worked for me at first. But after a certain time when I'm using nsys to profile a LLM process and it got stuck, I press ctrl-Z to stop it, but he no longer worked. Now if `ray_workers_use_nsight=False` it boots normally...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -Z to stop it, but he no longer worked. Now if `ray_workers_use_nsight=False` it boots normally, but `ray_workers_use_nsight=True` causes it to stuch when initialize nccl environment and warn is generated as below: ada6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: change. Addendum: I'm currently using docker and I don't know if this information will help me with my dilemma. Restarting the docker container does not resolve the issue. ### Before submitting a new issue... - [x] Make...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
