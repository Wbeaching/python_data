// 引入文件读写模块 系统默认包含fs模块 所以无需下载
var fs = require('fs')

var gameRoleInfo = {
    name : '德玛西亚',
    level : '18' ,
    equipment:['五速鞋','三速鞋','攻速鞋','水银鞋','布甲鞋','特步'],
    blood :'3500',
    attack : '111',
    money :'3201'
}
// 将字典对象转化成字符串对象 
var gameRoleInfoString = JSON.stringify(gameRoleInfo)

// writeFile后面跟三个值
// 1.写入文件的路径
// 2.写入的内容
// 3.写入以后的回调函数
fs.writeFile('data/game.txt',gameRoleInfoString,function(err){
    if(err)
    {
        console.log('文件写入失败:' + err)
    }
    else{
        console.log('文件写入成功')
    }
})
// readFile里面两个参数
// 参数1：读取的文件的路径
// 参数2：读取文件以后的回调函数
// 回调函数里面有两个参数
// 参数1：读取失败以后的信息
// 参数2：读取成功以后的信息
setTimeout(function(){
    fs.readFile('data/game.txt',function(err,data){
        if(err)
        {
            console.log('读取失败')
        }
        else{
            // JSON.parse 将字典格式的字符串转化成字典对象
            console.log('读取成功')
            console.log(JSON.parse(data))
        }
    })
},100)




