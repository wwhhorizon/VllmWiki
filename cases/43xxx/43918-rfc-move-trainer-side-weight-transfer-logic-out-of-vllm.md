# vllm-project/vllm#43918: [RFC]:  Move trainer-side weight transfer logic out of `vllm`

| 字段 | 值 |
| --- | --- |
| Issue | [#43918](https://github.com/vllm-project/vllm/issues/43918) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]:  Move trainer-side weight transfer logic out of `vllm`

### Issue 正文摘录

### Motivation. The new vLLM weight transfer APIs were introduced in https://github.com/vllm-project/vllm/pull/31943 (`vllm/distributed/weight_transfer/`). They give RL frameworks a standard way to sync updated weights from a trainer process into running vLLM workers, with pluggable backends (NCCL, CUDA IPC, etc.). Today, a backend is implemented by subclassing `WeightTransferEngine` and providing the below methods: ```python class MyWeightTransferEngine(WeightTransferEngine): init_info_cls = MyInitInfo update_info_cls = MyUpdateInfo # vLLM-side (receive) def init_transfer_engine(self, init_info: MyInitInfo): ... def receive_weights( self, update_info: MyUpdateInfo, load_weights: Callable[[list[tuple[str, Tensor]]], None], ): ... # Trainer-side (send) — called from the RL framework @staticmethod def trainer_send_weights( iterator: Iterator[tuple[str, Tensor]], trainer_args: dict[str, Any] | Any, ): ... ``` `init_transfer_engine` and `receive_weights` are vLLM-side logic for setting up transport and receiving weights into the worker. `trainer_send_weights` (and on `NCCLWeightTransferEngine` also `trainer_init`) is a helper meant to be called from the trainer process to send weights...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t_transfer_engine`, `receive_weights`, `shutdown`. - Keep the backend-specific request/info dataclasses (`*InitInfo`, `*UpdateInfo`) where they are. They define the wire format between trainer and vLLM and remain part o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rainer process into running vLLM workers, with pluggable backends (NCCL, CUDA IPC, etc.). Today, a backend is implemented by subclassing `WeightTransferEngine` and providing the below methods: ```python class MyWeightTr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lasses (`*InitInfo`, `*UpdateInfo`) where they are. They define the wire format between trainer and vLLM and remain part of the vLLM public API. - Provide **one reference implementation per backend** under `examples/rl/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: weights from a trainer process into running vLLM workers, with pluggable backends (NCCL, CUDA IPC, etc.). Today, a backend is implemented by subclassing `WeightTransferEngine` and providing the below methods: ```python...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: master_port: int, world_size: int, packed: bool = False, packed_buffer_size_bytes: int = DEFAULT_PACKED_BUFFER_SIZE_BYTES, packed_num_buffers: int = DEFAULT_PACKED_NUM_BUFFERS, ): # Trainer is rank 0 in the stateless pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
