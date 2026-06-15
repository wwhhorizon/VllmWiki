# vllm-project/vllm#13518: [Installation]: pip failed

| 字段 | 值 |
| --- | --- |
| Issue | [#13518](https://github.com/vllm-project/vllm/issues/13518) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: pip failed

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm (ds) C:\Users\ectek>pip install vllm -i https://pypi.tuna.tsinghua.edu.cn/simple/ Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/ Collecting vllm Using cached https://pypi.tuna.tsinghua.edu.cn/packages/69/1a/58ef1f5278d2039cdec4453c522c52f39b29b0ccbf7b8177d5766a99f8ec/vllm-0.7.2.tar.gz (5.4 MB) Installing build dependencies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting psutil (from vllm) Using cached https://pypi.tuna.tsinghua.edu.cn/packages/50/1b/6921afe68c74868b4c9fa424dad3be35b095e16687989ebbb50ce4fceb7c/psutil-7.0.0-cp37-abi3-win_amd64.whl (244 kB) Collecting sentencepiece (from vllm) Using cached https://pypi.tuna.tsinghua.edu.cn/packages/85/f4/4ef1a6e0e9dbd8a60780a91df8b7452ada14cfaa0e17b3b8dfa42cecae18/sentencepiece-0.2.0-cp310-cp310-win_amd64.whl (991 kB) Collecting numpy =2.26.0 in c:\users\ectek\miniconda3\envs\ds\lib\site-packages (from vllm) (2.32.3) Requirement already satisfied: tqdm in c:\users\ectek\miniconda3\envs\ds\lib\site-packages (from vllm) (4.67.1) Collecting blake3 (fro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: pip failed installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm (ds) C:\Users\ectek>pip install vllm -i https://pypi.tuna.tsinghua.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: running build_py creating build\lib\vllm copying vllm\beam_search.py -> build\lib\vllm copying vllm\config.py -> build\lib\vllm copying vllm\connections.py -> build\lib\vllm copying vllm\envs.py -> build\lib\vllm copyin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 89a59498/tiktoken-0.9.0-cp310-cp310-win_amd64.whl (894 kB) Collecting lm-format-enforcer =0.10.9 (from vllm) Using cached https://pypi.tuna.tsinghua.edu.cn/packages/32/55/9b91312b7b59903ffa2d1c4310cbeecfea0f8e8e12b154d7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: r\layers\fused_moe\configs\E=1,N=14336,device_name=NVIDIA_A100-SXM4-80GB,dtype=int8_w8a16.json -> build\lib\vllm\model_executor\layers\fused_moe\configs copying vllm\model_executor\layers\fused_moe\configs\E=1,N=14336,d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ying build\lib\vllm\model_executor\layers\quantization\kernels\scaled_mm\cutlass.py -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\quantization\kernels\scaled_mm copying build\lib\vllm\model_executor\layers...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
