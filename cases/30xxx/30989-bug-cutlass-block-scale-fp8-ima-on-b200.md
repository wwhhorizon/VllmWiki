# vllm-project/vllm#30989: [Bug]: CUTLASS BLOCK SCALE FP8 IMA on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#30989](https://github.com/vllm-project/vllm/issues/30989) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CUTLASS BLOCK SCALE FP8 IMA on B200

### Issue 正文摘录

### Your current environment B200 ### 🐛 Describe the bug Currently, CUTLASS BLOCK SCALE FP8 is broken on main. There are two problems. - A) it is impossible to use cutlass block scale fp8 in fp8.py, we pass `inplace=True` to `fused_experts`. In `fused_experts`, _valid_cutlass_block_scaled_group_gemm is always set to False, so it never triggers CUTLASS BLOCK SCALE FP8 https://github.com/vllm-project/vllm/blob/b0b77c46551bb5762a520f2b6e3af73a4defdfab/vllm/model_executor/layers/fused_moe/cutlass_moe.py#L950 - B) setting `inplace=False` in `fused_experts` allows us to trigger CUTLASS BLOCK SCALE FP8, however, when doing so, I get an IMA immediately ```bash MODEL := "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8" PORT := "8001" launch: VLLM_USE_DEEP_GEMM=0 VLLM_MOE_USE_DEEP_GEMM=0 chg run --gpus 1 -- vllm serve {{MODEL}} --enforce-eager --max-model-len 8192 --port {{PORT}} eval LIMIT: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" \ --limit {{LIMIT}} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUTLASS BLOCK SCALE FP8 IMA on B200 bug ### Your current environment B200 ### 🐛 Describe the bug Currently, CUTLASS BLOCK SCALE FP8 is broken on main. There are two problems. - A) it is impossible to use cutlass...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: use cutlass block scale fp8 in fp8.py, we pass `inplace=True` to `fused_experts`. In `fused_experts`, _valid_cutlass_block_scaled_group_gemm is always set to False, so it never triggers CUTLASS BLOCK SCALE FP8 https://g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: CUTLASS BLOCK SCALE FP8 IMA on B200 bug ### Your current environment B200 ### 🐛 Describe the bug Currently, CUTLASS BLOCK SCALE FP8 is broken on main. There are two problems. - A) it is impossible to use cutlass...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: CUTLASS BLOCK SCALE FP8 IMA on B200 bug ### Your current environment B200 ### 🐛 Describe the bug Currently, CUTLASS BLOCK SCALE FP8 is broken on main. There are two problems. - A) it is impossible to use cutlass...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/b0b77c46551bb5762a520f2b6e3af73a4defdfab/vllm/model_executor/layers/fused_moe/cutlass_moe.py#L950 - B) setting `inplace=False` in `fused_experts` allows us to trigger CUTLASS BLOCK SCALE FP8,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
