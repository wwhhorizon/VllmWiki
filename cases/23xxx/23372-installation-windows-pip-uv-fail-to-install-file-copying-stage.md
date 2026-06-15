# vllm-project/vllm#23372: [Installation]: Windows (pip & uv) fail to install (file copying stage)

| 字段 | 值 |
| --- | --- |
| Issue | [#23372](https://github.com/vllm-project/vllm/issues/23372) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Windows (pip & uv) fail to install (file copying stage)

### Issue 正文摘录

### Your current environment ```text python .\collect_env.py Traceback (most recent call last): File "C:\Users\Ingwie Phoenix\work\vllm\collect_env.py", line 19, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ``` This is the output I see in both `pip install vllm` and `uvx vllm`: ``` [stderr] C:\Users\Ingwie Phoenix\AppData\Local\uv\cache\builds-v0\.tmpDyTFqz\Lib\site-packages\torch\_subclasses\functional_tensor.py:276: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at C:\actions-runner\_work\pytorch\pytorch\pytorch\torch\csrc\utils\tensor_numpy.cpp:81.) cpu = _conversion_method_template(device=torch.device("cpu")) vLLM only supports Linux platform (including WSL) and MacOS.Building on win32, so vLLM may not be able to run correctly C:\Users\Ingwie Phoenix\AppData\Local\uv\cache\builds-v0\.tmpDyTFqz\Lib\site-packages\setuptools_scm\_integration\version_inference.py:51: UserWarning: version of None already set warnings.warn(self.message) listing git files failed - pretending there aren't any error: could not create 'build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs\E=128,N=3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Windows (pip & uv) fail to install (file copying stage) installation ### Your current environment ```text python .\collect_env.py Traceback (most recent call last): File "C:\Users\Ingwie Phoenix\work\v
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: l_executor\layers\fused_moe\configs\E=128,N=384,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory hint: This usually indicates a problem with the package or the build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: tor\layers\fused_moe\configs\E=128,N=384,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory hint: This usually indicates a problem with the package or the build environ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 't any error: could not create 'build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs\E=128,N=384,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or director...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d_moe\configs\E=128,N=384,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory hint: This usually indicates a problem with the package or the build environment. ``` ### H...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
