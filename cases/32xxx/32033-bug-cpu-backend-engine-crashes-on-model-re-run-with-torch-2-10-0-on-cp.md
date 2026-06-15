# vllm-project/vllm#32033: [Bug]: [CPU Backend]: Engine crashes on model re-run with torch=2.10.0 on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#32033](https://github.com/vllm-project/vllm/issues/32033) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend]: Engine crashes on model re-run with torch=2.10.0 on CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM Engine crashes on 2nd run with `torch==2.10.0` (it works fine with `torch==2.9.1`). The crash appears right after: `INFO 01-09 16:23:33 [decorators.py:435] Directly load AOT compilation from path /home/fadara01/.cache/vllm/torch_aot_compile/5ec3311dcd44687f4ab64740dffe375eddf7febd257d403c131aa1680ca1626f/rank_0_0/model` - see full logs below. If we manually remove `/home/fadara01/.cache/vllm/torch_aot_compile/5ec3311dcd44687f4ab64740dffe375eddf7febd257d403c131aa1680ca1626f/rank_0_0/model` the second run works fine **Steps to reproduce:** - Install torch 2.10.0 for CPU from https://dev-discuss.pytorch.org/t/pytorch-2-10-rc1-produced-for-pytorch-torchvision-torchaudio/3281 ``` pip3 install torch==2.10.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cpu ``` - Build vLLM with `torch==2.10.0` by running: `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - Run reproducer script below once -> it works fine - Run it again and you'll hit the error below, the `(EngineCore_DP0 pid=572512) INFO 01-09 16:23:33 [decorators.py:435] Directly load AOT compilation from path /home/fadara01/.cache/vllm/torch_aot_c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ctly load AOT compilation from path /home/fadara01/.cache/vllm/torch_aot_compile/5ec3311dcd44687f4ab64740dffe375eddf7febd257d403c131aa1680ca1626f/rank_0_0/model` - see full logs below. If we manually remove `/home/fadar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=False) llm = LLM(model=model_id, seed=0, dtype="bfloat16", ) params = SamplingParams( seed=0, max_tokens=128, temperature=0.7, top_p=0.9, top_k=50, ) results = llm.generate(messages_with_chat_template, p
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [CPU Backend]: Engine crashes on model re-run with torch=2.10.0 on CPU bug;cpu ### Your current environment ### 🐛 Describe the bug vLLM Engine crashes on 2nd run with `torch==2.10.0` (it works fine with `torch==2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: [CPU Backend]: Engine crashes on model re-run with torch=2.10.0 on CPU bug;cpu ### Your current environment ### 🐛 Describe the bug vLLM Engine crashes on 2nd run with `torch==2.10.0` (it works fine with `torch==2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 3c131aa1680ca1626f/rank_0_0/model` the second run works fine **Steps to reproduce:** - Install torch 2.10.0 for CPU from https://dev-discuss.pytorch.org/t/pytorch-2-10-rc1-produced-for-pytorch-torchvision-torchaudio/328...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
