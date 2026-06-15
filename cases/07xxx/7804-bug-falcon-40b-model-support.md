# vllm-project/vllm#7804: [Bug]: falcon-40B model support 

| 字段 | 值 |
| --- | --- |
| Issue | [#7804](https://github.com/vllm-project/vllm/issues/7804) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: falcon-40B model support 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when use `tiiuae/falcon-40b` model for offline_inference.py, it will throw such error: ``` [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/model_loader/loader.py", line 170, in _initialize_model [rank0]: return build_model( [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/model_loader/loader.py", line 155, in build_model [rank0]: return model_class(config=hf_config, [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/models/falcon.py", line 389, in __init__ [rank0]: self.transformer = FalconModel(config, cache_config, quant_config) [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/models/falcon.py", line 350, in __init__ [rank0]: self.h = nn.ModuleList([ [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/models/falcon.py", line 351, in [rank0]: FalconDecoderLayer(config, cache_config, quant_config) [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/models/falcon.py", line 249, in __init__ [rank0]: if (config.num_ln_in_parallel_attn is None [rank0]: File "/home/sdp/miniforge3/envs/ipex_ww32/lib/python3.10/site-packages/transformers/configuration_utils.py", line 264, in __getattr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: falcon-40B model support bug;stale ### Your current environment ### 🐛 Describe the bug when use `tiiuae/falcon-40b` model for offline_inference.py, it will throw such error: ``` [rank0]: File "/home/sdp/kunshang/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: el_loader/loader.py", line 170, in _initialize_model [rank0]: return build_model( [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/model_loader/loader.py", line 155, in build_model [rank0]: return model_class(...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: falcon-40B model support bug;stale ### Your current environment ### 🐛 Describe the bug when use `tiiuae/falcon-40b` model for offline_inference.py, it will throw such error: ``` [rank0]: File "/home/sdp/kunshang/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: init__ [rank0]: self.transformer = FalconModel(config, cache_config, quant_config) [rank0]: File "/home/sdp/kunshang/vllm/vllm/model_executor/models/falcon.py", line 350, in __init__ [rank0]: self.h = nn.ModuleList([ [r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
